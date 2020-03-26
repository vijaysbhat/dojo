# CS Problems & Solutions

## Common Patterns

<details>
  <summary>
    Canonical Data Structure Operations in Python

* HashMap    
* Stack
* Queue
* Heap
    
  </summary>
### HashMap
```
d = {}
d['a'] = 2
d['b'] = 1
'b' in d
=> True
del d['b']
'b' in d
=> False
d.get('b')
=> None
```

### Stack  
```
stack = []
stack.append('a')
stack.append('b')
stack.pop()
=> 'b'
'a' in stack
=> True
stack.pop()
=> 'a'
```
### Queue
```
# Method 1
from collections import deque 
q = deque()
q.append('a') 
q.append('b')
q.popleft()
=> 'a'
'b' in q
=> True
q.popleft()
=> 'b'

# Method 2
from Queue import Queue 
q = Queue()
q.put('a') 
q.put('b')
q.get()
=> 'a'
'b' in q
=> TypeError: argument of type 'instance' is not iterable
q.get()
=> 'b'

```

### Heap
```
from heapq import heappush, heeppop
h = []
heappush(h, 'a')
heappush(h, 'c')
heappush(h, 'b')
heappop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: heappop() takes exactly one argument (0 given)
heappop(h)
'a'
heappop(h)
'b'
heappop(h)
'c'
```
</details>

<details>
  <summary>
    Common Operations

* Create a list of n integers / characters  
* Sort a dict / array of tuples
    
  </summary>

### Create a list of n integers / characters
```
l = [0] * n    # create a list of n zeroes
```
### Sort a dict / array of tuples
```
# sort by second element in descending order
sorted_arr = sorted(arr, lambda x: x[1], reverse=True)
sorted_dict = sorted(d, lambda x: x['key'])
```
</details>

## Questions
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
