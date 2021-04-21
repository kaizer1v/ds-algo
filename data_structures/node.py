'''
Node is a single element

[i]         - is a node with the element `i` inside it
[head]      - is a head node
[tail]      - is a tail node
'''

class Node:

    def __init__(self, elm, nxt=None):
        self._elem = elm
        self._next = nxt

    def __repr__(self):
        return '[{}] ->'.format(self._elem)


class NodeLR(Node):
    '''
    This is Node that is connected
    on both sides, left & right. Used in
    `reverse-able linked list` type of data strutures
    '''
    def __init__(self, elem=None):
        super(NodeLR, self).__init__(elem)
        self._prev = None
        self._next = None

    def __repr__(self):
        return 'None <- [{}] -> None'.format(self._elem)
