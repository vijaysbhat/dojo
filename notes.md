
## Code Review Checklist
* Create test cases - normal and degenerate valued. e.g.
  * Odd and even length palindrome matches.
  * Odd and even length arrays for finding medians.
  * Duplicates in arrays
  * Empty and null strings / arrays.
* Validate input size and return values for degenerate cases.
* Store the length of the array in a variable.
* Array counters being initialized correctly esp. for nested loops.
* Array counters are being incremented in all the required locations.
* Can integer values be negative? Can there be overflow / underflow?
* All branches of conditional (if/else) statements being explicitly handled.
* Linked list - all pointers that need to be advanced are being advanced.
* Validate logic works in termination case as well e.g. right after breaking out of a loop
* Set visited flag for graph traversal.
* Keep talking through ways to improve solution after getting the basic implementation right.
* Python specific
  * Append to a list in a separate statement and return the variable in the following statement. List append returns None in Python.
  * When calculating mid point of two array indexes, cast as int. Otherwise Python converts to float which will cause an index exception.
  * Initializing a 2-D array gotcha - `[[0] * m] * n` doesn't work since it creates an array of n references to the same row! Use `[[0] * m for i in range(n)]` instead to create a m x n array.

## Problem Solving Patterns
* Sorting
* Hash table
* Recursion
* Divide and conquer - identical subproblems
* Dynamic programming - overlapping subproblems
* Greedy algorithms - locally optimum solutions at each iteration
* Invariants
  * Given a sorted array, common pattern is to use pointers starting from either end moving inwards. e.g. 2-sum problem, maximum water trapped between vertical lines. 


## Algorithm Notes

### Asymptotic Complexity Recursive Formulas
| Formula  | Solution  | Examples  | 
|---|---|---|
| `T(n) = T(n/2) + O(1)`|`O(log n)`|Binary search|
|`T(n) = T(n-1) + O(1)`|`O(n)`|Sequential search|
|`T(n) = 2 T(n/2) + O(1)`|`O(n)`|Binary tree traversal|
|`T(n) = T(n-1) + O(n)`|`O(n^2)`|Selection sort|
|`T(n) = 2 T(n/2) + O(n)`|`O(n log n)`|Quicksort|
|`T(n) = T(n/2) + O(n)`|`O(n)`|Median / k-th largest element|

### Quicksort partitioning logic
* Two techniques - [Hoare's](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme) (what I learned in school) and [Lomuto's](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
* Handling duplicates of the pivot element in Hoare's partitioning
  * Duplicates of the pivot element **can go into either subarray**. We don't need to pick a side for duplicates to go to (I had thought we needed to) because the sort will ultimately converge after further partitioning iterations. More on this in these [lecture notes](https://www.cs.princeton.edu/courses/archive/spring09/cos226/lectures/06Quicksort-2x2.pdf)
  * This means we include a check for equality to the pivot also when detecting inverted pairs of elements (**arr[l] >= pivot, arr[r] <= pivot**)
* Dutch National Flag approach
  * Three way partitioning scheme invented by Djikstra - bottom, middle (equal to pivot element), top
  * Use 3 indexes for lesser (initialize to 0), equal (initialize to 0) and higher (initialize to len(arr)-1) and iterate through array in a single pass
  
### Bloom Filter
* Probabilistic data structure for testing if a key is in a set - false positives are possible but false negatives are not
  * hash the key and check if the bit at that index is set
  * if the bit is not set we definitely know the key is not present
  * if the bit is set, we know with a probability threshold (1 - hash collision probability) that the key is present, so we need to check for actual presence.
* Used in BigTable / HBase, CDNs, browser caches (detect second request for a web object and only then cache)


### String Search

* Three O(n) algorithms - KMP, Boyer-Moore and Robin Karp
* Robin-Karp easiest to understand
  * Replace string comparisons with hash based **fingerprint** comparisons
  * A **rolling** hash allows reuse of the previous substring hash value as the sliding window for comparison advances in the larger string
* **Steps**
  * Take the hash of the smaller substring (size m).
  * Starting from the beginning of the larger string (size n) advance a sliding window comparing hash value with the smaller string and incrementally updating the hash value.
  * If there is a match of hash values, check for an actual match because there could be a hash collision.
* **O(m+n)** run time as long as the hash function doesn't have a lot of collisions

### Binary Search Trees

* [Deletion](https://en.wikipedia.org/wiki/Binary_search_tree#Deletion)
  * Node has no children - trivial
  * Node has one child - swap child with node to be deleted
  * Node has two children
    * Find successor to node in right subtree and replace value in node to be deleted.
    * If replacement node has children, it's only a right child - update replacement node's parent to point to that child node.
    * Delete replacement node.
  * **NOTE** no tree rotation operation required.
  
### Graph Algorithms

* Dijkstra's shortest path
  * Steps
    * Initialize all nodes as unvisited, create a lookup table of distance to source initialized to infinity / None.
    * Set source node distance to zero (by definition) and add node to priority queue.
    * Get the node from the priority queue with the minimum distance value. **<< KEY STEP**
    * For each unvisited neighbor, update its distance value to the source if the path through the current node is shorter.
    * Mark the current node as visited and repeat the loop until the target is reached.
  * Greedy algorithm and can take a very meandering path
  * Correctness reasoning - when we get the minimum distance valued node from the priority queue, it satisfies the shortest path property to the source. Why? If there were a shorter path, it would have to traverse from the set of visited nodes to the unvisited nodes, back to the visited nodes and then the currently selected node. If that were the case, a node in the previous section of the path in the unvisited nodes should have been selected from the priority queue. **This is why the positive edge weights requirement is crucial.**
* A* algorithm - directed shortest path
  * Improves upon Dijkstra by using the currently known *true* distance to the source plus a heuristic distance (known ahead of time, e.g. Euclidian distance) so more promising paths are explored first.
  * Correctness - if the heuristic distance is guaranteed to be less than or equal to the true distance, we can trivially see that it will give us the correct result.

### Streaming algorithms
  * [Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
    * Maintain random sample of k elements (without replacement) from stream
    * Read first k elements from stream
    * Maintain count of elements seen so far, n
    * For n > k, generate a random number i from 0 to n-1
      * If i < k replace the element in the sample at position i with the new element
      * If i >= k, discard the new element
  * k-minimum values
    * cardinality estimation (approximate count distinct) in high cardinality datasets
  * [Hyper-log-log](https://en.wikipedia.org/wiki/HyperLogLog)
    * cardinality estimation (approximate count distinct) in high cardinality datasets
  * [Count-min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)
    * frequency count for high cardinality datasets
    * data structure: two-dimensional array of w columns and d rows
    * d hash functions for each row, h_d
    * when new event with key k arrives, for each row d compute h_d(k) and increment the count in that column
    * for a point query for key k, return min(count[d, h_d(k)]) over all rows
  * Top-k frequent keys
    * need the following data structures
      * count-min sketch for count lookup and update
      * min-heap for storing top k frequency elements
      * hash table of size k for fast lookup by key
    * when new event arrives
      * lookup and update the frequency for its key in the count-min sketch
      * if the key exists in the hash table, increment its count there
      * if the key doesn't exist in the hash table
        * test if the count is greater than the count for smallest top-k key from the min-heap.
          * if yes, evict the smallest key from the min-heap and replace with the new key. replace the hash table entry for the evicted key with the new key
          * if no, discard the new key and move on to the next event
* [MinHash](https://en.wikipedia.org/wiki/MinHash)
  * fast approximation for Jaccard Similarity
  
### Stream Processing Model
* Useful for reasoning about unbounded datasets - pretty much every real world example.
* Batch is a special case of stream processing.
* Event time vs processing time.
* Watermark is the a function of processing time p_t - maximum event time e_t <= p_t such that every event time e_t' <= e_t has arrived.
* Fixed window, rolling window and dynamic (session) window processing.
* Triggers - when to materialize the window. Can materialize at periodic intervals until the watermark and then for every late arriving data element within the lateness horizon of the watermark.
* Resources
  * https://www.oreilly.com/radar/the-world-beyond-batch-streaming-101/
  * https://www.oreilly.com/radar/the-world-beyond-batch-streaming-102/


## Other Concepts

### Multithreading

* Java
  * Implement Runnable interface
  * Extend Thread class (limiting due to lack of multiple inheritance in Java)
* Synchronization
  * synchronized methods in the object (class or instance)
  * synchronized block
  * locks
* Python
  * Not possible to do truly concurrent multithreading (i.e. utilize multicore CPU) due to GIL
  * Useful for I/O heavy tasks that wait on resources being available
  * No improvement for CPU heavy tasks
  * Use ThreadPoolExecutor from concurrent.futures
  * Use threading.Lock to synchronize control


### Object Oriented Design

* Practice questions
  * Design an ATM
  * Design an elevator
  * Design a Parking System
  
### SQL 

* Use [CTEs](https://en.wikipedia.org/wiki/Hierarchical_and_recursive_queries_in_SQL#Common_table_expression) liberally
* Windowing functions
  * Lead / Lag - e.g. find previous / next quantity bought
  ```
  lag(qty,1) over (partition by buyerid order by saletime) as prev_qty
  lead(qty,1) over (partition by buyerid order by saletime) as next_qty
  ```
  * Cumulative sum - e.g. find quantity bought so far
  ```
  saletime,
  sum(qty) over (partition by buyerid order by saletime rows unbounded preceding) as cum_sum
  ```
  * Sliding window sum
    * e.g. backward looking 7 day rolling sum of quantity bought
    ```
    saletime,
    sum(qty) over (partition by buyerid order by saletime rows 7 preceding) as prev7day_sum
    ```
    * e.g. forward looking 7 day rolling sum of quantity bought
    ```
    saletime,
    sum(qty) over (partition by buyerid order by saletime rows 7 following) as next7day_sum
    ```
  * First value / last value
    * e.g. find time of first and last purchase per buyer
    ```
    first_value(saletime) over (partition by buyerid order by saletime) as first_purchase_time,
    last_value(saletime) over (partition by buyerid order by saletime) as last_purchase_time
      ```
  * Rank
    * Use row_number() instead of rank() since rank() can have duplicates
    * e.g.find latest purchases by each buyer
    ```
    row_number() over (partition by buyerid order by saletime desc) as rnk
    ...
    where rnk = 1
    ```
  * Percentile
    * e.g. find top 50% of purchases by quantity
    ```
    percent_rank() over (partition by buyerid order by qty) as pctile
    ...
    where pctile > 0.5
    ```
* Review resources
  * https://docs.aws.amazon.com/redshift/latest/dg/r_Window_function_examples.html
