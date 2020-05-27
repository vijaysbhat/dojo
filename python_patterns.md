# Common Python Patterns

* [Canonical Data Structure Operations in Python](#canonical-data-structure-operations-in-python)
  * [HashMap](#hashmap)    
  * [Stack](#stack)
  * [Queue](#queue)
  * [Heap](#heap)
* [Common Operations](#common-operations)
  * [Substring / subarray](#substring--subarray)
  * [Create a list of n integers / characters](#create-a-list-of-n-integers--characters)  
  * [Sort a dict / array of tuples](sort-a-dict--array-of-tuples)
  * [Flatten a 2 level nested list](#flatten-a-2-level-nested-list)
  * [Trim a string (use strip)](#trim-a-string)

## Canonical Data Structure Operations in Python

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
# Python 3
from queue import Queue 
q = Queue()
q.put('a') 
q.put('b')
q.get()
=> 'a'
'b' in q
=> TypeError: argument of type 'instance' is not iterable
q.get()
=> 'b'

# Method 2
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

```

### Heap
```
# Method 1 - PriorityQueue
# Python 3
# A typical pattern for entries is a tuple in the form: (priority_number, data).
# items are retrieved in increasing order of priority_number

from queue import PriorityQueue 
pq = PriorityQueue()
pq.put((1, 'a'))
pq.put((3, 'b'))
pq.put((2, 'z'))
pq.get()
=> (1, 'a')
pq.empty()
=> False
pq.get()
=> (2, 'z')
pq.get()
=> (3, 'b')

# Method 2 - limited use since you can only push and pop values
from heapq import heappush, heappop
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

## Common Operations
      
### Substring / subarray
```
ss = s[i:j]      #inclusive of index i, exclusive of index j
sarr = arr[i:j]

s[i:i]          # if i == j, empty string / array is returned
>> ''
arr[i:i]
>> []
```
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
### Flatten a 2 level nested list
```
non_flat = [ [1,2,3], [4,5,6], [7,8] ]
[y for x in non_flat for y in x]

>> [1, 2, 3, 4, 5, 6, 7, 8]
```
### Trim a string
```
# removes trailing and leading whitespace
s.strip()
```

