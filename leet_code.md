<details>
  <summary>
  <b>Container with most water</b>
  
  Given a set of n parallel vertical lines with heights represented in an array, find the two lines that along with the X-axis can contain the maximum volume of water.  
  
  <b>Insight:</b> 
  Start with outermost lines and moving the shorter line inward with each step since that's the only way the volume can increase.
  </summary>
  
```
class Solution(object):
    def volume(self, p, q):
        return min(p[1], q[1]) * abs(p[0]-q[0])
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        coords = [(i, h) for i, h in enumerate(height)]
        n = len(coords)
        i = 0
        j = n-1
        max_vol = 0
        while i < j:
            max_vol = max(max_vol, self.volume(coords[i], coords[j]))
            if coords[i][1] < coords[j][1]:
                i += 1
            else:
                j -= 1
        return max_vol

```
</details>
<details>
  <summary>
  <b>Longest substring without repeating characters</b>
  
  Given a string, find the length of the longest substring without repeating characters.
  
  <b>Insight:</b> 
  Sliding window pattern with the start and end of the window moving independently in a single loop
  </summary>
  
```
class Solution(object):    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_substr_len = 0
        if len(s) <= 1:
            return len(s)
        
        max_substr_len = 0        
        char_dict = {}
        i = 0
        j = 0
        substr_len = 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in char_dict.keys():
                char_dict[s[j]] = 1
                j += 1
                max_substr_len = max([max_substr_len, j - i])
            else:
                del char_dict[s[i]]
                i += 1
                    
        return max_substr_len

```

</details>
<details>
  <summary>
  <b>Find median of two sorted arrays</b>
  
  <b>Insight:</b> 
  Use binary search in the smaller sized array to find partition locations in both arrays where boundary elements on one side of the partition are smaller than the boundary elements on the other side of the partition.
  
  Good patterns for reasoning about boundary conditions
  </summary>
  
https://leetcode.com/articles/median-of-two-sorted-arrays/

```
class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # pattern: when doing binary search type of operations use variables to
        #   * store the length of the subarrays
        #   * calculate 1 indexed locations of elements within the subarrays
        #   * subtract 1 to get actual index location
        # makes it much easier to reason about edge cases and stopping conditions
        # rather than manipulating the zero indexed element locations
        if len(A) > len(B):
            return self.findMedianSortedArrays(B, A)
        m = len(A)
        n = len(B)
        
        imin = 0
        imax = m
        
        while imin <= imax:
            i = (imin + imax)/2
            j = (m + n + 1)/2 - i
            # handling edge cases
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and B[j] < A[i-1]:
                imax = i - 1
            else:
                if i == 0:
                    left_max = B[j-1]
                elif j == 0:
                    left_max = A[i-1]
                else:
                    left_max = max(A[i-1], B[j-1])
                if (m+n) % 2 == 1:
                    return left_max
                
                if i == m:
                    right_min = B[j]
                elif j == n:
                    right_min = A[i]
                else:
                    right_min = min(A[i], B[j])
                    
                return (left_min + right_min) / 2.0
                    
```
</details>
<details>
  <summary>
  <b>Longest palindromic substrings</b>
    
  <b>Insight:</b> Use dynamic programming 
  </summary>
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

<b>Notes:</b> 
* Use while loop instead of for loop since it is better for explicitly controlling boundary condition
* Check whether counter is being incremented in while loop
* Check whether if statements with multiple clauses if all condition combinations are being handled explicitly, otherwise will cause unpredictable behavior
* Python substring operator is exclusive of second operand
* Loop termination boundary condition - write out equation for constraints with all relevant variables and rearrange 
* Dynamic programming - bottom up approach is easier to reason about and place correctness guarantees on
```
class Solution(object):
    def is_palindrome(self, s, memo, i, j):
        if i == j:
            memo[(i,j)] = True
            return True
        if j == i + 1:
            if s[i] == s[j]:
                memo[(i,j)] = True
                return True
            else:
                memo[(i,j)] = False
                return False
        
        if memo[(i+1, j-1)] == True and s[i] == s[j]:
            memo[(i,j)] = True
            return True
        memo[(i,j)] = False
        return False
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {}
        n = len(s)
        l = 1
        i = 0
        max_len = 0
        max_str = ''
        while l <= n:
            i = 0
            while i < n - l + 1:
                if self.is_palindrome(s, memo, i, i+l-1) and max_len < l:
                    max_str = s[i:i+l]
                i += 1
            l += 1
        return max_str
```
</details>

<details>
  <summary>
  <b>Regular expression matching</b>

  <b>Insight:</b> Use dynamic programming 
  </summary>
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
  
  <b>Notes</b>
* dynamic programming memo indexed by string location tuples
* Top down approach - could also have done bottom up working backwards from the ends of both strings
```
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def match(i, j):
            if (i,j) not in memo:
                if j >= len(p):
                    ret = (i == len(s))
                else:
                    first_char_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
                    if j+1 < len(p) and p[j+1] == '*':
                        ret = match(i, j+2) or (first_char_match and match(i+1, j))
                    else:
                        ret = first_char_match and match(i+1,j+1)
                memo[(i,j)] = ret
            return memo[(i,j)]
        
        return match(0,0)
```
</details>

<details>
  <summary>
  <b>Longest matching parantheses</b>    
    
  <b>Insight:</b> Use stack based approach
  </summary>
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
      
  <b>Notes:</b>
  
* Stack based solution more intuitive
* Think of alternatives a bit before running to a DP approach

https://leetcode.com/problems/longest-valid-parentheses/solution/

```
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        ret = 0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if (len(stack) == 0):
                    stack.append(i)
                else:
                    ret = max([ret, i - stack[-1]])
        return ret
```
</details>

<details>
  <summary>
  <b>Merge k sorted linked lists</b>
    
  <b>Insight:</b> Use heap / priority queue 
  </summary>
<b>Notes</b>

* Use queue.PriorityQueue (put and get) for heap API
* Linked list trick - use a dummy head to make initialization logic cleaner, throw away before returning linked list (return head.next)

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        head = current_node = ListNode(0)

        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            next_node = node.next
            current_node.next = ListNode(val)
            current_node = current_node.next
            if next_node:
                q.put((next_node.val, next_node))
        return head.next
```
</details>
