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
  * [Relational Database scaling](#relational-database-scaling)
  * [Message queues](#message-queues-and-async-processing) to decouple backend processing
* **Resource Isolation**
* **Backend Database Choice**
  * [SQL vs NoSQL](#sql-vs-nosql)
* **Availability Numbers**
  * 3 nines downtime
    * ~100 seconds per day
    * ~10 hours per year
  * 4 nines downtime
    * ~10 seconds per day
    * ~1 hour per year
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
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from 1 Gbps  10,000,000   ns   10,000 us   10 ms  40x memory, 10X SSD
Read 1 MB sequentially from disk    30,000,000   ns   30,000 us   30 ms 120x memory, 30X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms 3000x data center round trip

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

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
    * set of packets that are sent without gating on ACK
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
  * Three way / five way handshake
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

### Multithreading

### Unique ID Generation

* Needed for transaction processing
* Client side vs server side
  * easier dedupe multiple submissions of same request
  * can be a security liability in case of buggy / malicious clients
  * distributed server side solution more complex
  * use Twitter snowflake or UUID library with collision guarantees

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
  * Two phase lock
  * row level, table level

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
  * increased application.
  * uneven shard key can cause unbalanced load on shards.
  * use consistent hashing to reduce resharding data movement.  
* **denormalization**
  * pre-join tables
  * can improve read performance
  * write performance can be poor if all denormalized tables need to be synced
* **SQL tuning**
  * benchmark - ab
  * profile - slow query tool
  * use indexes + NOT NULL
    * NULLS cause full scan
  * use CHAR instead VARCHAR.
    * searching is faster since end of string doesn't need to be found before moving onto next one.

### NoSQL
* KV / document store
  * e.g. MongoDB, DynamoDB
* Wide column store
  * e.g.BigTable, HBase
* Graph DB
  * e.g. Neo4J

### SQL vs NoSQL

* SQL
  * schema guarantees structure and quality
  * transactions
  * joins
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

### Consistent Hashing

* Fundamental algorithm behind CDNs (Akamai)

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


## Papers

* Facebook memcached
* Chubby
* DynamoDB

## Resources

* https://github.com/donnemartin/system-design-primer
* https://tianpan.co/notes/2016-02-13-crack-the-system-design-interview/
* https://www.the-paper-trail.org/post/2008-11-27-consensus-protocols-two-phase-commit/
* https://www.the-paper-trail.org/post/2008-11-29-consensus-protocols-three-phase-commit/
* https://landing.google.com/sre/sre-book/toc/
