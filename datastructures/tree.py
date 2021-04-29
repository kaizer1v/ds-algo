'''
Tree

Tree is a data structure that has at least 2 nodes
attached to a single node (if not then it's a linked list)

                    ['a']
                    /   \
                ['b']   ['c']
                /   \      \
            ['d']  ['e']   ['f']

If it has at-max 2 nodes attached to a another, it's called
a "Bi-nary" tree.

WHY?
Searching takes O(n) in an ordered linked-list (as you need to iterate
through the entire linked-list to find the correct element), while it
takes O(log n) in a binary tree (BST) because, at each node, you can
either look left or right, effectively splitting the input in roughly half

While insert and delete can theoretically be performed in O(1) in a
linked-list, you need to search for the correct position to insert or
find the element to delete first, so these operations will also take
O(n), as opposed to a BST, where they take O(log n)
'''
class TreeNode:

    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

class Tree(TreeNode):
    '''
    This is a tree where each node has at most 2 nodes attached
    to it i.e. to the left or to the right
    '''
    def __init__(self):
        self.root = TreeNode(None)

    def __repr__(self):
        # traverse through the tree
        pass
