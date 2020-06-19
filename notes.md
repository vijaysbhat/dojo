
## Code Review Checklist
* Input size and return values for degenerate cases.
* Array counters are being incremented in all the required locations.
* Store the length of the array in a variable.
* All branches of conditional (if/else) statements being explicitly handled.
* Linked list - all pointers that need to be advanced are being advanced.
* Python specific
  * Append to a list in a separate statement and return the variable in the following statement. List append returns None in Python.
  * Initializing a 2-D array gotcha - `[[0] * n] * m]` doesn't work since it creates an array of m references to the same row! Use `[[0] * n] * i for i in range(m)]` instead.

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


### String search

* Three O(n) algorithms - KMP, Boyer-Moore and Robin Karp
* Robin-Karp easiest to understand
  * Replace string comparisons with hash based *fingerprint* comparisons
  * A *rolling* hash allows reuse of the previous substring hash value as the sliding window for comparison advances in the larger string
* **Steps**
  * Take the hash of the smaller substring (size m).
  * Starting from the beginning of the larger string (size n) advance a sliding window comparing hash value with the smaller string and incrementally updating the hash value.
  * If there is a match of hash values, check for an actual match because there could be a hash collision.
* **O(m+n)** run time as long as the hash function doesn't have a lot of collisions

