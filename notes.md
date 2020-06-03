
## Code Review Checklist
* Input size and return values for degenerate cases.
* Array counters are being incremented in all the required locations.
* Store the length of the array in a variable.
* All branches of conditional (if/else) statements being explicitly handled.
* Linked list - all pointers that need to be advanced are being advanced.
* Python specific
  * Append to a list in a separate statement and return the variable in the following statement. List append returns None in Python.
  * Initializing a 2-D array gotcha - `[[0] * n] * m]` doesn't work since it creates an array of m references to the same row! Use `[[0] * n] * i for i in range(m)]` instead.


## Algorithm Notes

### Quicksort partitioning logic
* Two techniques - [Hoare's](https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme) (what I learned in school) and [Lomuto's](https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme)
* Handling duplicates of the pivot element in Hoare's partitioning
  * Duplicates of the pivot element **can go into either subarray**. We don't need to pick a side for duplicates to go to (I had thought we needed to) because the sort will ultimately converge after further partitioning iterations. More on this in these [lecture notes](https://www.cs.princeton.edu/courses/archive/spring09/cos226/lectures/06Quicksort-2x2.pdf)
  * This means we include a check for equality to the pivot also when detecting inverted pairs of elements (**arr[l] >= pivot, arr[r] <= pivot**)
* Dutch National Flag approach
  * Three way partitioning scheme invented by Djikstra - bottom, middle (equal to pivot element), top
  * Use 3 indexes for lesser (initialize to 0), equal (initialize to 0) and higher (initialize to len(arr)-1) and iterate through array in a single pass
