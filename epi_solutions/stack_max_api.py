'''
Implement a stack class with a max API
Notes:
* 
* what went right
    * remembered pattern of storing max values in a separate stack
* bugs
    * forgot to check for size of max stack before checking top element
'''

class Stack(object):
    def __init__(self):
        self.arr = []
        self.max_arr = []

    def push(self, el):
        self.arr.append(el)
        if len(self.max_arr) == 0 or self.max_arr[-1] <= el:
            self.max_arr.append(el)

    def pop(self):
        ret = self.arr.pop()
        if len(self.max_arr) > 0 and self.max_arr[-1] == ret:
            self.max_arr.pop()
        return ret


    def max(self):
        return self.max_arr[-1]


if __name__ == '__main__':
    test_cases = [
        [1,2,10,5,4,11],
        [1,2,12,5,4,11],
        [1,11,10,2,11],
        [1]
    ]
    for i, t in enumerate(test_cases):
        s = Stack()
        print('Test case', i)
        for el in t:
            s.push(el)
            print(el, s.max_arr, s.max())
