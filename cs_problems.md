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


## Questions

<details>
  <summary>
  <b>Longest Substring Without Repeating Characters</b>
  
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
