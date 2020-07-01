'''
Reverse a linked list.

Notes
* Iterative solution was a grind to get the variables right
* Recursive solution had a bug with the tail element of the reversed list not having a null next value

'''


class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(arr):
    prev_node = None
    head = None
    for el in arr:
        node = Node(el)
        if head is None:
            head = node
        if prev_node is not None:
            prev_node.next = node
        prev_node = node
    return head

def print_list(node):
    i = 0
    while node is not None and i < 10:
        print(node.val)
        node = node.next
        i += 1

def reverse_list(x):
    new_head = None
    while x is not None:
        next_x = x.next
        x.next = new_head
        new_head = x
        x = next_x
    return new_head

def reverse_list_recursive_helper(x):
    if x is None:
        return None, None
    if x.next is None:
        return x, x
    head, tail = reverse_list_recursive_helper(x.next)
    tail.next = x
    return head, x

def reverse_list_recursive(x):
    head, tail = reverse_list_recursive_helper(x)
    tail.next = None
    return head

if __name__ == '__main__':
    test_cases = [
         [1,2,3,4,5]
    ]
    for t in test_cases:
        print_list(reverse_list(create_list(t)))
        print_list(reverse_list_recursive(create_list(t)))
