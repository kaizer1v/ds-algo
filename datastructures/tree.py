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
class BiTreeNode:

    def __init__(self, elem, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right

class BinaryTree(BiTreeNode):
    '''
    This is a tree where each node has at most 2 nodes attached
    to it i.e. to the left or to the right
    '''
    def __init__(self):
        self.root = BiTreeNode(None)

    def __repr__(self):
        # traverse through the tree
        pass

    def add(self, elem, left=None, right=None):
        '''
        Add at most 2 nodes

        Parameters
        ----------
        left : str, int
            the value of the left node
        right : str, int
            the value of the right node

        Returns
        -------
        self
        '''
        n = Node(elem)
        if self.root == None:
            self.root = n
        # if new elem is gt the root
        if self.root < n.elem:
            n.left = self.root
        # if new elem is lt the root
        else:
            n.right = self.root
        self.root = n
        return self





'''
To Create
        4
       / \
      9   2     <-- Keep adding at this level
     / \ / \
    N  NN  N

Now add (6, 8) to the tree, will become

        4
       / \
      6   8     <-- Keep adding at this level
     /     \
    9       2
   / \     / \
  N  N    N  N

'''
bt = BinaryTree(4)
bt.add(9, 2)

