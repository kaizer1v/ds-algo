'''
Node is a single element

[i]         - is a node with the element `i` inside it
[head]      - is a head node
[tail]      - is a tail node
'''

class Node:

    def __init__(self, elem=None):
        self.elem = elem
        self.next = None

    def __repr__(self):
        return '[{}] -> None'.format(self.elem)

    def is_head(self):
        '''
        Is a node a `head` node?
        '''
        return self.elem == None

    def is_tail(self):
        '''
        Is a node the `tail` node?
        '''
        return self.next == None
