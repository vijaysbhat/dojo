# Common Python Patterns

* [Canonical Data Structure Operations in Python](#canonical-data-structure-operations-in-python)
  * [HashMap](#hashmap)    
  * [Stack](#stack)
  * [Queue](#queue)
  * [Heap](#heap)
* [Common Operations](#common-operations)
  * [Substring / subarray](#substring--subarray)
  * [Initialize a list of n integers / characters](#initialize-a-list-of-n-integers)  
  * [Initialize a m x n array of integers / characters](#initialize-an-array-of-integers)  
  * [Sort a dict / array of tuples](#sort-a-dict--array-of-tuples)
  * [Flatten a 2 level nested list](#flatten-a-2-level-nested-list)
  * [Trim a string (use strip)](#trim-a-string)
  * [Append to a string / array](#append-to-a-string--array)
  * [Iterate over array with index and element](#iterate-over-array-with-index-and-element)
  * [Iterate over dict key value pairs](#iterate-over-dict-key-value-pairs)
  * [Convert between integers and characters](#convert-between-integers-and-characters) 
  * [Get unique strings from a list of strings](#get-unique-strings-from-a-list-of-strings)

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
### Initialize a list of n integers
```
l = [0] * n    # create a list of n zeroes
```

### Initialize an array of integers
```
# the construct [[0] * m] * n] doesn't work since it reuses references 
# to the inner list, not what we want.
arr = [[0] * m for i in range(n)]    # create a m x n array of zeroes
```

### Sort a dict array / tuple array
```
# sort by second element of array of tuples in descending order
sorted_arr = sorted(arr, key=lambda x: x[1], reverse=True)

# sort an array of dicts by an attribute e.g. d = {'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
sorted_dict = sorted(d, key=lambda x:x['age'])

# sort dict by value e.g. d = {'b':1, 'a':2}
{k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
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

### Append to a string / array
```
arr = [1,3,10]
arr.append(7)
print(arr)
>> [1, 3, 10, 7]
arr.extend([2,3])
print(arr)
>> [1, 3, 10, 7, 2, 3]

s = 'abcd'
s = s + 'e'
print(s)
>> abcde
s = s + 'fg'
print(s)
>> abcdefg

```

### Iterate over array with index and element
```
arr = [1,3,10]
for i, el in enumerate(arr):
    print(i, el)

>> 0 1
>> 1 3
>> 2 10
```

### Iterate over dict key value pairs
```
 d = {1:2, 2:3}
 for k, v in d.items():
     print(k,v)
>> 1 2
>> 2 3
```

### Convert between integers and characters  
```
ord('a')
>> 97
ord('A')
>> 65
ord('0')
>> 48
ord('9')
>> 57
chr(ord('0') + 7)
>> '7'
```

### Get unique strings from a list of strings
Convert to a set and back to a list
```
arr = ['abc', 'abc', 'xyz']
list(set(arr))
>> ['xyz', 'abc']
```
