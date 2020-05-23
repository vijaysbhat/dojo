### Container with most water
  
  Given a set of n parallel vertical lines with heights represented in an array, find the two lines that along with the X-axis can contain the maximum volume of water.  
  
  <b>Insight:</b> 
  Start with outermost lines and moving the shorter line inward with each step since that's the only way the volume can increase.
  
[Solution](/leet_code/container_most_water.py)

### Longest substring without repeating characters
  
  Given a string, find the length of the longest substring without repeating characters.
  
  <b>Insight:</b> 
  Sliding window pattern with the start and end of the window moving independently in a single loop

[Solution](/leet_code/longest_substring_no_repeating_chars.py)

### Find median of two sorted arrays
  
  <b>Insight:</b> 
  Use binary search in the smaller sized array to find partition locations in both arrays where boundary elements on one side of the partition are smaller than the boundary elements on the other side of the partition.
  
  Good patterns for reasoning about boundary conditions
  
https://leetcode.com/articles/median-of-two-sorted-arrays/

[Solution](/leet_code/median_two_sorted_arrays.py)


### Longest palindromic substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

<b>Insight:</b> Use dynamic programming 

[Solution](/leet_code/longest_palindromic_substring.py)


### Regular expression matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

<b>Insight:</b> Use dynamic programming 

[Solution](/leet_code/regular_expression_matching.py)

  
### Longest matching parantheses   
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
    
<b>Insight:</b> Use stack based approach

https://leetcode.com/problems/longest-valid-parentheses/solution/

[Solution](/leet_code/longest_matching_parantheses.py)


### Merge k sorted linked lists</b>
    
<b>Insight:</b> Use heap / priority queue 

[Solution](/leet_code/merge_k_sorted_linked_lists.py)

