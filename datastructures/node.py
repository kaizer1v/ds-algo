'''
Node is a single entity that is used in other data structures like Linked List or Stacks. Each element
of a Linked List or a Stack is called a node. A node has two properties

1. Element (contains the data of the node)
2. Link (A link to the next node). There can be more than 1 link to the node i.e. left or right or multiple as well

Example:
[i] -> None         - is a node with the element `i` inside it & it points to another node which is `None`
'''

class Node:
    '''
    Basic Node
    '''

    def __init__(self, elem=None, nxt=None):
        self.elem = elem
        self.next = nxt

    def __repr__(self):
        return '[{}] ->'.format(self.elem)


class NodeLR(Node):
    '''
    This is Node that is connected
    on both sides, left & right. Used in
    `reverse-able linked list` type of data strutures
    '''
    def __init__(self, elem=None):
        super(NodeLR, self).__init__(elem)
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'None <- [{}] -> None'.format(self.elem)
