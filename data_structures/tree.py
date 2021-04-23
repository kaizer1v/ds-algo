from node import NodeLR

class Tree:
    '''
                    ['a']
                    /   \
                ['b']   ['c']
                /   \      \
            ['d']  ['e']   ['f']

    This is a tree where each node has at most 2 nodes attached
    to it i.e. to the left or to the right
    '''

    def __init__(self):
        pass

    '''
    Question is how do you store such a tree?
    {
        'a': ['b', 'c']
        'b': ['d', 'e']
        'c': ['f']
    }
    can be one way of storing this, but is it efficient?
    1. Can I search an element in the tree in `O(n)` time?
    2. What if I remove a node from the centre of the tree? How will I reorg the tree?
    '''
