
'''
Test if a binary tree satisfies the BST property

Notes:
* what went right
    * remembered the pattern of using multiple return values
    * implemented BFS solution with no errors
* what went wrong
    * didn't review that left_min, left_max, right_min and right_max were getting set correctly 
      in the base case for recursive solution
'''
from queue import SimpleQueue

class BinaryTree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder_print(self):
        if self.left is not None:
            print('traverse left')
            self.left.inorder_print()
        print(self.val)
        if self.right is not None:
            print('traverse right')
            self.right.inorder_print()

def is_binary_tree(tree):
    '''
    Return whether the tree is balanced and the min and max values in the tree
    '''
    if tree is None:
        return True, None, None
    left_balanced, left_min, left_max = is_binary_tree(tree.left)
    right_balanced, right_min, right_max = is_binary_tree(tree.right)
    if left_balanced == False or right_balanced == False:
        return False, None, None
    left_min = left_min or tree.val
    left_max = left_max or tree.val
    right_min = right_min or tree.val
    right_max = right_max or tree.val
    if left_max <= tree.val and tree.val <= right_min:
        return True, left_min, right_max
    else:
        return False, None, None     

def is_binary_tree_bfs(tree):
    q = SimpleQueue()
    q.put(tree)
    while q.empty() == False:
        node = q.get()
        if (node.left is not None and node.left.val > node.val) or (node.right is not None and node.right.val < node.val):
            return False
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)
    return True

def create_tree_from_node_list(nodes):
    node_dict = {}
    # setup nodes
    for el in nodes:
        node_dict[el[0]] = BinaryTree(el[0])
    # setup pointers
    for el in nodes:
        node = node_dict[el[0]]
        if el[1]:
            node.left = node_dict[el[1]]
        if el[2]:
            node.right = node_dict[el[2]]
    return node_dict[nodes[0][0]]

if __name__ == '__main__':
    test_cases = [
        [(19,7,43), (7,3,11), (3,2,5), (2,None,None), (5,None,None), (11,None,17), (17,13,None), (13,None,None),
         (43,23,47), (23,None,37), (37,29,41), (29,None,31), (31,None,None), (41,None,None), (47,None,53), (53,None,None)],
        [(314,6,7),(6,271,561),(271,None,None),(561,None,None),(7,None,None)]
    ]

    for t in test_cases:
        tree = create_tree_from_node_list(t)
        #tree.inorder_print()
        print(is_binary_tree(tree))
        print(is_binary_tree_bfs(tree))
