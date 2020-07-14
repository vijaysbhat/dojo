# System Design Notes

## Areas Of Concern

* **Security**
  * Authentication
  * Authorization
  * Audit
  * Privacy / PII / Confidential data
  * Malicious Attacks
* **Scaling**
  * [Load balancer](#load-balancer)
  * Horizontal stateless scaling
  * Caching layer
    * Application cache vs database cache
      * database cache more transparent
    * Write-through vs read-through cache
      * write-through reduces stampede on backend DB.
      * write-through cache makes writes slower but users more tolerant of write slowness than read slowness.
    * Write behind (async DB update)
    * Scaling - Redis / Memcached
      * scales to ~100k qps (~2 ms latency) vs MySQL ~10k qps (~25 ms latency)
      * network bandwidth generally gets exhausted (1-10 Gbps) before CPU
  * [Relational Database scaling](#relational-database-scaling)
  * [Message queues](#message-queues-and-async-processing) to decouple backend processing
* **Resource Isolation**
* **Storage**
  * KV store cluster
  * Graph DB cluster
  * Blobstore cluster
  * Analytics cluster
  * CDN
* **Backend Database Choice**
  * [SQL vs NoSQL](#sql-vs-nosql)
* **Availability Numbers**
  * 3 nines downtime
    * ~100 seconds per day
    * ~10 hours per year
  * 4 nines downtime
    * ~10 seconds per day
    * ~1 hour per year
* **Deployment**
  * CI / CD
  * Staged rollout (staging, canary, prod %)
  * Small holdout to compare changes to previous version
  * Kill switches and feature flags
* **Observability & Monitoring**
  * Log ingestion and indexing - Kibana
  * Real time metrics - statsd, Grafana
  * Pager alerts on thresholds
* **Stress Tesing & SLA**
  * Benchmarking tool like ab
  * Profiling tool like MySQL slow queries log
* **Fault Tolerance & Disaster Recovery**
  * Fail-over patterns
    * Active-active
    * Active-passive
  * [Thundering herd](#thundering-herd)
  * Traffic bursts and events
    * Prioritize incoming requests, gracefully degrade / backpressure / rate limit / drop lower priority requests
    * Pre-provision for known events - automated system?
  * Use of DNS for transparent switchover

## Latency Numbers
```
Latency Comparison Numbers
--------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy            10,000   ns       10 us
Send 1 KB bytes over 1 Gbps network     10,000   ns       10 us
Read 4 KB randomly from SSD*           150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us           4GB/sec
Round trip within same datacenter      500,000   ns      500 us          5000x main memory reference
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
Redis query latency                  2,000,000   ns    2,000 us    2 ms
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
MySQL query latency                 25,000,000   ns   25,000 us   25 ms
Read 1 MB sequentially from disk    30,000,000   ns   30,000 us   30 ms 30MB/sec, 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms 3000x data center round trip

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

General rule of thumb:
--------------
nanosecond scale - CPU operations
microsecond scale - memory, SSD operations
millisecond scale - network, disk operations
```

## Power of twos

```
Power           Exact Value         Approx Value        Bytes
---------------------------------------------------------------
7                             128
8                             256
10                           1024   1 thousand           1 KB
16                         65,536                       64 KB
20                      1,048,576   1 million            1 MB
30                  1,073,741,824   1 billion            1 GB
32                  4,294,967,296                        4 GB
40              1,099,511,627,776   1 trillion           1 TB
```

## Concepts

### Networking
#### DNS

* UDP on port 53
* Multi level caching with TTL
* Record types
  * A record -> IP address
  * CNAME -> A record or CNAME
  * NS record - DNS name server
  * MX record - Mail exchange server
* Can be used for
  * Geo-aware load balancing
  * Keeping traffic away from servers under maintenance

#### CDN

* Push vs Pull (On-demand) CDN
* Use for high popularity / traffic content

#### OSI model

* **Layer 1 - Physical**
  * Data encoding and transmission
  * e.g. Ethernet, 802.11 physical layers, DSL
* **Layer 2 - Link**
  * **Identifier** - IP address
  * Node to node link
  * **ARP** = Address Resolution Protocol i.e. IP address -> MAC address discovery for IPv4
  * **NDP** = Neighbor Discovery Protocol i.e. IP address -> MAC address discovery for IPv6
  * Collision detection / avoidance and retransmission
    * **CSMA / CD** (Carrier Sense Multiple Access with Collision Detection) - Ethernet
    * **CSMA / CA** (Carrier Sense Multiple Access with Collision Avoidance) - 802.11
  * e.g. Ethernet, PPP, 802.11, ARP
* **Layer 3 - Network**
  * **Identifier** - IP address
  * Routing
  * IPv4 - 32 bits
  * IPv6 - 128 bits
    * Loopback - ::1
  * IPSec
    * Transport mode - IP headers not encrypted but data is
    * Tunnel mode - original IP headers also encapsulated and encrypted -> VPN
  * Routing table
    * network ID - destination subnet
    * metric - cost
    * next hop - address of next node
  * Subnet
    * CIDR (Classless Inter Domain Routing) e.g. 198.51.100.0/24 covers the range 198.51.100.0 to 198.51.100.255
    * Subnet mask e.g. 255.255.255.0 is the subnet mask for the prefix 198.51.100.0/24
  * OSPF (Open Shortest Path First)
    * sends hello packets to neighboring routers to update link state and cost
    * doesn't use TCP / UDP but IP datagrams
* **Layer 4 - Transport**
  * Flow control
  * Message segmentation & ack
  * Session multiplexing
  * **Identifier** - client IP address + port
* **Layer 5 - Session**
  * Sessions between processes running on different hosts
  * e.g. RPC, SQL
* **Layer 6 - Presentation**
  * Syntax layer - encrypt and decrypt if needed
  * e.g. ASCII, JPEG
* **Layer 7 - Application**
  * e.g. HTTP, FTP, SMTP


#### TCP / IP model (Internet Protocol Suite)

* **Link Layer**
* **Internet Layer**
* **Transport Layer**
* **Application Layer**

![Data Flow](/images/networking_data_flow.png)
![Data Encapsulation](/images/networking_data_encapsulation.png)

**Note** - Sockets (ip address + port + transport) are a transport layer concept (layer 4) i.e. both a TCP and UDP application can bind to port 53



#### TCP
  * **three way handshake**
    * SYN - client to server
    * SYN / ACK - server to client
    * ACK - client to server
  * randomly generated **sequence number**
  * no concept of session id, **client address + port** is used instead
  * **packet / segment loss detection**
    * no ACK received before RTO (retransmission timeout)
    * resend segment - **fast retransmit**
    * enter congestion avoidance state
  * **congestion window**
    * set of TCP segments that are sent without waiting for ACK from receiver
    * maintained by sender to prevent *link* from getting overloaded
  * **receive (sliding) window**
    * used for flow control
    * advertised by receiver to prevent *receiver* from getting overloaded 
    * packets received out of order are rearranged in order within the receive window
  * **slow start**
    * congestion window set to 1 MSS (maximum segment size)
    * increased by 1 for each ACK received, which doubles the window size each round trip delay time (RTT)
  * **congestion avoidance**
    * AIMD - Additive Increase Multiplicative Decrease
    * increase congestion window size linearly if no packet loss
    * decrease congestion window size exponentially if packet loss detected

#### TCP vs UDP

* TCP
  * guaranteed delivery
  * automatic adaptation to network throughput
  * throughput gated by round trip latency due to ACKs
* UDP
  * Low latency
  * Use when late data is worse than data loss
  * DHCP uses UDP because client doesn't yet have an IP address
  * e.g. video streaming, gaming

#### What happens after clicking on a web link

* DNS resolution
  * Browser cache
  * OS cache
  * Router cache
  * ISP DNS server
* TCP / TLS connection
  * Three way handshake for TCP and additional two roundrips for TLS for certificate exchange.
  * Client port bound to connection and listening for responses from server
* HTTP request payload constructed with headers
* Packaged into TCP packets with headers
* Packaged into IP packets with headers
* Packaged into link layer frames with headers
* Hops across routers until it reaches destination server
* Link layer frames unpacked
* IP layer packets unpacked
* TCP layer packets unpacked and HTTP request payload reconstructed
* Server builds HTTP response payload and sends back to client in similar manner.
* Client reconstructs HTTP response payload and displays in the browser.


### Load Balancer

* SSL termination at the load balancer / nginx
  * reduces the CPU load on downstream services
  * removes the need to install SSL certificates everywhere
* Routing strategies - along with health checks
  * Random
  * Round robin
  * Level 4 (transport layer)
    * IP address + port based
  * Level 7 (application layer)
    * e.g. video traffic routed to video servers

### Unique ID Generation

* Needed for transaction processing
* Client side vs server side
  * easier dedupe multiple submissions of same request
  * can be a security liability in case of buggy / malicious clients
  * distributed server side solution more complex
  * use libraries
    * Twitter snowflake
      * coordination by zookeeper
      * 64 bits
    * UUID library with collision guarantees
      * 128 bits

### Database Concurrency

* **CAP theorem** [paper](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf) and [example](https://mwhittaker.github.io/blog/an_illustrated_proof_of_the_cap_theorem/).
  * **Consistency** - any read operation that begins after a write operation completes must return that value, or the result of a later write operation.
  * **Availability** - every request received by a non-failing node in the system must result in a response
  * **Partition tolerance** - the network will be allowed to lose arbitrarily many messages sent from one node to another. **This requires specifying a threshold for how out-of-date the data can get.**
* **ACID properties**
  * Atomicity - all or nothing transactions
  * Consistency - all database constraints must be satisfied
  * Isolation - transactions must not interfere with each other
  * Durability - committed transactions persist through crashes
* **Optimistic concurrency**
  * If transactions have modified the data after the current transaction's start timestamp, abort and rollback.
* **Multiversion concurrency control**
  * Generate new versions of database objects on writes  
* **Locking mechanisms**
  * Transactions
    * START TRANSACTION -> COMMIT
    * Implemented through write ahead logging, shadow pages and two phase locking for guaranteeing full isolation
  * Two phase lock
    * Lock expanding phase
    * Lock shrinking phase

### Database Indexes
* B Tree / B+ Tree
  * Node types
    * Internal nodes - min of L children and max of U children
    * Root node - same upper limit U but no lower limit
    * Leaf nodes
  * Optimize lookup in block storage devices due to high fanout
  * B+ Tree specifies records stored in leaf nodes
* Hash Index
  * O(1) for point queries
  * Range queries O(n)
* Log Structured Merge Tree
  * Provides indexed access to files with high write volume, like  transaction log data
  * Data stored in two or more separate tree structures (e.g. one in memory and the other on disk) and data is synchronized between them in rolling batches (compaction)


### Distributed system consensus
  * Two phase commit
    * Propose / vote phase
    * Commit / abort phase
    * Can block indefinitely if coordinator fails in the middle of phase 1 or 2
  * Three phase commit
    * Prepare to commit phase after the proposal phase and before the commit phase.
    * Coordinator does not send commit message until all members have ACKed that they are prepared to commit, which means no member can commit a transaction before all members are aware of the decision to do so.
    * Removes possibility of indefinite blocking unlike two phase commit.
    * Three round trip times (RTT) make transactions slow.
  * Paxos
  * Raft

### Relational Database Scaling
* **master-slave replication**
  * when master is down, operate in read-only mode until slave promoted to master.
* **master-master replication**
  * allows read-write mode even when one of the masters is down.
  * synchronization and conflict resolution hard between masters.
* **federation**
  * split up databases by function e.g.users, products etc.
  * smaller database size, less traffic and replication.
  * complex to do joins across function.
* **sharding**
  * data split across databases by shard key.
  * reduces read / write traffic and replication.
  * increased application complexity.
  * uneven shard key can cause unbalanced load on shards.
  * use consistent hashing to reduce resharding data movement.  
* **denormalization**
  * pre-join tables
  * can improve read performance
  * write performance can be poor if all denormalized tables need to be synced
* **SQL tuning**
  * benchmark high load situations - ab
  * profile - slow query tool
  * use indexes + NOT NULL
    * NULLS cause full scan
  * use CHAR instead VARCHAR.
    * searching is faster since end of string doesn't need to be found before moving onto next one.

### NoSQL
* KV / document store
  * e.g. MongoDB, DynamoDB
  * How is it different from Redis cache (also persisted to disk)?
    * Cache is presumed to fit entirely in memory with disk as backup
    * KV / document store can be petabytes large and makes no assumption of fitting in memory
* Wide column store
  * e.g.BigTable, HBase
* Graph DB
  * e.g. Neo4J

### Consistent Hashing

* Uses
  * Fundamental algorithm behind CDNs (Akamai)
  * Distributed hash tables
* How does it work?
  * Map each key to a point on a circle (or equivalently, mapping each key to a real angle).
  * Map each available machine (or other storage bucket) to many pseudo-randomly distributed points on the same circle. Number of points each server maps to is configurable.  
* Placing a key
  * Find the location of the key on the circle
  * Walk around the circle until the first server / bucket encountered
* Resizing the cluster
  * Add / remove all the points on the circle corresponding to the new / invalid servers
  * Remap keys to the closest server point on the circle.
  * Due to random distribution of server points on the circle, the redistribution is balanced across servers.  
* Time complexity - K keys and N slots

||Classic Hash Table|Consistent Hashing|
|--|--|--|
|add a node|O(K)|O(K/N + log N)|
|remove a node|O(K)|O(K/N + log N)|
|add a key|O(1)|O(log N)|
|remove a key|O(1)|O(log N)|

* Mapping **each server to multiple points on the circle** is what achieves the O(K/N) property for resizing. Otherwise a server going down would require all keys for that server to mapped to the next server in the circle, doubling its load.


### SQL vs NoSQL

* SQL
  * schema guarantees structure and quality
  * transactions
  * joins
    * hash join
    * merge join
  * well established scaling patterns
  * index lookups
  * table size limit - 32TB on PostGres
* NoSQL
  * ease of development and quick iterations
  * no joins
  * no ACID guarantees
  * can scale to petabytes


### Data Protection
  * Replication
    * Identical copies of data
    * e.g. RAID, HDFS
  * Erasure coding
    * Parity / information theory based technique
    * Less storage
    * More compute
    
### Data Storage Formats

#### [Parquet](https://databricks.com/session_eu19/the-parquet-format-and-performance-optimization-opportunities)
* Data orginization - hybrid of row and columnar formats
  * Row groups (128 MB)
  * Column chunks
    * Pages (1 MB)
      * Metadata (min / max / count)
      * Encoded values (plain or RLE dictionary)
        * If dictionary gets too big, reduce row group size.
* Predicate pushdown through 
  * skip entire row groups through min/max statistic, needs to be (semi)sorted on key to be useful.
  * dictionary filtering
* Optimization
  * directory based partitions
  * avoid small files - compaction
      
### Data Serialization Formats

* [Protobuf](https://developers.google.com/protocol-buffers/docs/proto3)
* Thrift serialization
* JSON

### Message Queues And Async Processing

* Decouple expensive operations and push to a background worker
* RabbitMQ (AMQP), Amazon SQS, Kafka
* Queueing - single consumer receives any given message
* PubSub - many consumers can subscribe to a queue / topic
* Backpressure
  * Send HTTP 503 / failure codes when queue fills up and let client do exponential backoff.

### Kafka Internals
 * Order guaranteed at a partition level.
 * **Queueing** - use a single consumer group, messages load balanced across consumers.
 * **PubSub** - use multiple consumer groups, messages sent to each subscribed consumer group.
 * **Consumer position coordination**
   * Each partition is consumed by exactly one consumer in a consumer group, so only need to maintain one offset per partition per consumer group, which can be checkpointed.
 * **Exactly once semantics**
   * Store offset in the same location as the output data, guaranteeing that both the data and offset are updated or neither is e.g. Kafka Connect writes offset to HDFS


### RPC vs REST

* RPC
  * flexible definition of actions / behaviors
  * RPC libraries implement battle tested strategies for well behaved client logic
    * exponential backoff
    * add jitter to request time
    * load balancing and failover
    * [cascading cancelations](https://landing.google.com/sre/sre-book/chapters/addressing-cascading-failures/) (to avoid work doomed to be rejected due to timeouts)
  * caching is hard
  * e.g. gRPC (Protobuf), Thrift, Avro
* REST
  * stateless - horizontal scaling, sharding, caching is easy
  * operations limited to HTTP verbs and CRUD operations



### Thundering Herd
* When it happens
  * Read through cache miss for a new / updated popular item
    * Use write through cache instead
  * By poor design in server frameworks
    * [uWSGI vs gunicorn](https://uwsgi-docs.readthedocs.io/en/latest/articles/SerializingAccept.html)
    * [gevent](http://www.gevent.org/) and [greenlet](https://greenlet.readthedocs.io/en/latest/)
  * System comes back online after being down for some time
    * Server side
      * LIFO queue to process requests that aren't about to time out on the client (and will be retried anyway)
      * Drop old requests - takes care of badly behaved clients
    * Client side
      * Add jitter to request retry timing
      * Exponential backoff
      * Use a library like gRPC that implements all these


### Zero Copy
* Traditionally reading from a filesystem and writing to a socket / NIC involves two system calls and user / kernel context switches and a copy into application memory.
* Zero copy directly reads from a file into the socket / NIC in the kernel context avoiding the application memory copy.

### Real World Architectures

#### Instagram
* photos stored as blobs on S3 and replicated to CDNs
  * storing photos in a file system is suboptimal due to high amount of redundant metadata
  * use CDNs for popular / high traffic content
  * Facebook Haystack paper
* distributed id generation
  * autoincrement makes sharding impossible
* data model for users, posts and follows
  * joins at request time to serve feed gets expensive
* feeding frenzy paper
  * fanout after post ingest for feed precompute
  * backfilling for new follows
  * celebrity fanout too expensive - too many followers => too many backend jobs
  * serve hybrid of precomputed feed with merged of subscribed celebrity feeds - cardinality of celebrities low so can merge at feed request time

#### Chat server

* Clarify
  * one to one or group chat?
  * end to end encryption?
  * send files?
* Session has to be initiated by client (firewalls etc), so need long lived connections for server to push updates to client
  * Options - websockets, BOSH, HTTP long polling  
* Challenges
  * Presence - communicate to O(num_users * churn_rate * avg_friends) end points => 10s of millions of messages per second
  * Long lived connections hard on server since it has to keep state for all concurrent connections
  * Isolation is hard due to long lived nature and statefulness of requests.
* Components
  * Load balancer
  * Horizontally scaled API end point nodes - websocket connection means any given client talks to a single backend node
  * Distributed cache - Redis
    * Store heartbeat information and which node is managing connection for a user
    * Scaling Redis - master slave replicas
    * Can all heartbeat data fit in memory? 100GB per Redis node, 10 node cluster should work
  * NoSQL DB for storing messages (HBase / Cassandra)
* Flow
  * User A messages user B
  * Node managing user A will lookup heartbeat cache for what node is managing user B
  * Forward the message to node managing user B
  * This node sends the message to user B.
  * Persist message to NoSQL DB
* Use blob storage when sending images
* Group chat - use group membership table

#### Google Autocomplete

* Possible approaches
  * Trie for partial match lookup, each trie node stores match weight
  * ElasticSearch indexed by partial match with match weights
* Serving components
  * Load balancer
  * Horizontally scaled API end point nodes
  * Distributed cache
  * Distributed trie / ElasticSearch sharded by consistent hash
  * Zookeeper to get which Trie node / ElasticSearch shard to hit
* Background update mechanism
  * Rolling swap of shards - update shard location in Zookeeper

#### [Dropbox](https://www.youtube.com/watch?v=PE4gwstWhmc)

* Challenges
  * write volume
    * 10s millions of users
    * 100s of millions of file syncs
    * Read to write ratio 1:1
  * ACID requirements
    * Deleted files need to be deleted in every copy
* Evolution
  * 1 server with DB, store data on disk
    * ran out of disk space and server got overloaded
  * Moved to external MySQL and S3 storage
    * Server got overloaded again
  * Split into notification server, metadata server and block server
    * Added memcache tier and load balancer
    * Memcache consistency across cluster nodes is hard   
    * Load balancer hard due to Python GIL
    * Sharding DB was hard because of single MySQL assumptions baked into code - joins, transactions etc
      * How do you shard users and shared folders tables? Not obvious answer
* Single notification server running 1 million connections per machine! Hard to bring back up when they go down so don't push to the limit.
* Chunk files into 4MB pieces and re-upload if hash value is different
  * [Rsync](https://en.wikipedia.org/wiki/Rsync#Determining_which_parts_of_a_file_have_changed) like mechanism
* Metadata DB
  * server_file_journal - log of all edits made to a file

#### [Stripe Rate Limiter](https://stripe.com/blog/rate-limiters)
  * Rate limiting
    * Request rate limiter - N requests per user per second
    * Concurrent requests rate limiter - N requests in flight
    * Send HTTP 429 - Too many requests error
  * Load shedding
    * Prioritize requests into categories
    * Shedding needs to happen slowly to prevent flapping
    * HTTP 503 - Service unavailable
  * [Token bucket algorithm](https://en.wikipedia.org/wiki/Token_bucket)
    * Tokens added at a fixed rate and discarded when bucket limit reached.
    * When request comes in, if the bucket is empty reject. Otherwise serve the request and remove a token
    * One token bucket per user in Redis
    * Exact opposite of [leaky bucket](https://en.wikipedia.org/wiki/Leaky_bucket)
    * Or can use [TTL keys](https://redislabs.com/redis-best-practices/basic-rate-limiting/) in Redis

#### tinyURL Service
* Shortened string can be any string with 6 letters containing [0-9, a-z, A-Z]. That is, 62^6 ~= 64^6 -> 2^36 -> 64 billion unique strings
* Base conversion from unique ID to base 62 and back for shortened URL.
* Unique ID generation
  * Single DB - autoincrement is fine.
  * Distributed DB
    * UUID (128 bits), Twitter Snowflake (64 bits)
      * With 64 bit / 128 bit IDs, need a 11 char / 22 char shortened string which would be too long.
    * Cluster of servers doing autoincrement IDs.
      * Round robin ID generation requests to servers.
      * Prepend server index to generated ID.
      * What happens if one of the machines goes down? => **Need to keep track of the last ID generated**
        * Write messages to Kafka each time an ID is generated and replay when bringing the server back up.
        * Checkpoint IDs to disk and when bringing back up start from last checkpoint and increment counter until no matches found in mapping store.  
* Storage and expiry of mappings
  * Can store in HBase since it's a sparse key value store with TTL functionality
* Redirection
  * Off the shelf webserver sending a HTTP 303 response with the URL looked up from HBase

#### Hive
* Mapreduce translation - use a framework like Calcite to:
  * parse and validate SQL
  * translate SQL to logical plan
  * translate logical plan to physical plan (sequence of MR jobs)
* https://cwiki.apache.org/confluence/display/Hive/Design

#### Mapreduce
* InputFileSplitter
  * one split per map
* Map function
  * Emits intermediate key value pairs
* Partition function
  * Partition intermediate keys to destination reducers.
  * This is where you can address data skew
* Combiner
  * Pre-aggregate results on mapper before sending to reducer
* Shuffle sort
  * Mapper sorts output records by intermediate key
  * Reducer pulls records from all mappers for the intermediate keys assigned to it and merges them to get a sorted list of records.
  * How does reducer know which machines to pull from?
    * This information is relayed through mapper status updates to the job tracker / application master which sends it to the reducer via the heartbeat mechanism.
  * Why does reducer need sorted records?
    * So that it knows when it is done reducing a given intermediate key and can move on to the next one.
  * Reducer
    * Emits final key value records

#### HBase
* Architecture
  * High throughput indexed writes through [log structured merge tree](#database-indexes)
  * Regions
    * Range of rows between a start key and end key
  * Region servers
    Assigned multiple (~1000) regions
  * Master
    * Assign regions on startup
    * Monitor region server instances
    * Reassign regions for load balancing
    * Admin operations on tables
  * Zookeeper
    * Coordinate and share state between master and region server
* Use [Bloom Filter](/notes.md#bloom-filter) to avoid disk lookups for testing if column exists for a row
* Read path
  * Get region server for .META table from Zookeeper - cache for future use and refresh if there is a miss
  * Get region server for the table and row key
  * Retrieve the row from the region server
* Write path
  * Get region server for the row key in the same manner as for reads
  * Puts written to WAL (write ahead log) and MemStore
  * When MemStore threshold reached, flushed to disk as HFile
  * When number of HFiles reaches threshold, compaction kicks in


#### Elasticsearch
* Architecture
  * [Inverted index](https://www.elastic.co/blog/found-elasticsearch-from-the-bottom-up) data structure.
    * Index is sharded and replicated across multiple nodes.
  * Queries received by coordinator and broadcast to all nodes.
  * Dedicated ingest node to perform transformations in ingest path. 
  * Monitoring
    * Indexing buffer size
    * Cache misses
    * CPU usage
    * OOM errors
* Typical performance - 20qps at 500ms latency

#### Spark
* RDD - Resilient Distributed Dataset
  * **Transformations** on an RDD produce a new RDD e.g. map, filter, join, repartition
  * **Actions** on RDD produce results in memory e.g. reduce, count, collect
* RDD partitions are the fundamental unit of atomicity
* Dependencies mapped out with parent RDDs through the lineage DAG
* Stage
  * All operations that can be done without a shuffle are combined into a stage
* Checkpoint RDDs to disk
* Failure recovery
  * re-traverse lineage from closest upstream RDDs
  * recover from RDD checkpoints - can produce a lot of network traffic

## Resources

* https://github.com/donnemartin/system-design-primer
* https://tianpan.co/notes/2016-02-13-crack-the-system-design-interview/
* https://landing.google.com/sre/sre-book/toc/
* [Jeff Dean's Stanford talk](https://static.googleusercontent.com/media/research.google.com/en//people/jeff/stanford-295-talk.pdf) - **SOLID content**
* https://www.the-paper-trail.org/post/2008-11-27-consensus-protocols-two-phase-commit/
* https://www.the-paper-trail.org/post/2008-11-29-consensus-protocols-three-phase-commit/
* [Facebook memcached paper](https://www.usenix.org/system/files/conference/nsdi13/nsdi13-final170_update.pdf)

