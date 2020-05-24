'''
Take two sorted linked lists L, R and return the merge of L and R

Notes:
* when declaring a python class, inherit from object if not otherwise specified
* in the python class __init__ function, self is a required first argument
* next is a reserved name (iterator method) in python. use the variable name next_node for the pointer field instead.
* what went right
    * used dummy linked list head pattern
* bugs
    * forgot to advance the merged list node pointer variable
'''
class LinkedListNode(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def print_nodes(self):
        print(self.val)
        if self.next_node is not None:
            self.next_node.print_nodes()

def merge_lists(l, r):
    dummy_head = LinkedListNode(0)
    node = dummy_head
    while True:
        if l is None:
            node.next_node = r
            break
        if r is None:
            node.next_node = l
            break
        if l.val < r.val:
            node.next_node = l
            l = l.next_node
        else:
            node.next_node = r
            r = r.next_node
        node = node.next_node

    return dummy_head.next_node


def create_list_from_arr(arr):
    dummy_head = LinkedListNode(0)
    node = dummy_head
    for el in arr:
        next_node = LinkedListNode(el)
        node.next_node = next_node
        node = next_node
    return dummy_head.next_node


if __name__ == '__main__':
    test_cases = [
        ([1,4,6,10], [2,3,5]),
        ([1,4,6,10], []),
        ([], [2,3,5]),
        ([1,2,3], [4,5,6]),
    ]
    for t in test_cases:
        l = create_list_from_arr(t[0])
        r = create_list_from_arr(t[1])
        print(t)
        merge_lists(l,r).print_nodes()
