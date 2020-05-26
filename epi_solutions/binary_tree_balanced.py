'''
Check if a binary tree is balanced.

Notes:
* what went right
    * remembered how to calculate binary tree height
    * remembered balanced tree is a recursive requirement
'''

class BinaryTree(object):
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

    def inorder_print(self):
        if self.left is not None:
            print('traverse left')
            self.left.inorder_print()
        print(self.index)
        if self.right is not None:
            print('traverse right')
            self.right.inorder_print()

    def height(self):
        left_height = 0
        right_height = 0
        if self.left is not None:
            left_height = self.left.height()
        if self.right is not None:
            right_height = self.right.height()
        return max(left_height, right_height) + 1
    
    def is_balanced_height(self):
        left_balanced = True
        left_height = 0
        right_balanced = True
        right_height = 0
        
        if self.left is not None:
            left_balanced, left_height = self.left.is_balanced_height()
        if self.right is not None:
            right_balanced, right_height = self.right.is_balanced_height()

        is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = max(left_height, right_height) + 1
        return is_balanced, height

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
        [('A','B','C'), ('B','D',None), ('C',None,None), ('D',None,None)],
        [('A','B',None), ('B','D',None), ('D',None,None)],
    ]
    for i, t in enumerate(test_cases):
        print('>> test case', i)
        bt = create_tree_from_node_list(t)
        # bt.inorder_print()
        # print('tree height', bt.height())
        print('is balanced?', bt.is_balanced_height())
