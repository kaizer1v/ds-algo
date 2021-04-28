'''
Priority Queue

Prioritiy queue operates just like a queue, but when `pop`-ing
out the first element that was added, it instead takes out the
highest (max) element from the queue. Thus, the items in the
priority queue should be comparable. When you add a new item
into the queue, it will automatically remove the min value so
that the size of the queue remains fixed.

WHY?
One could always use a normal queue, sort it (desc) and then pop
the first one (max). NO - this isn't efficient because, doing that
the memory required will be `N` (size of the items in the queue) and
the sorting time will take `n log(n)` time, but using a Priority
Queue will do that in `n log(m)` and the space required will be `m`
only where m < n

IMPLEMENTATION
The implementation can be done using a linked list or a binary tree.
Either way, the data structure (DS) will always be sorted as soon as you
insert an item in the DS.
'''

class PriorityQueueUsingLinkedList:
    pass


class PriorityQueueUsingBinaryTree:

    def __init__(self):
        pass

    def swim(self):
        '''
        Moves the item up in order
        of the tree
        '''
        pass

    def sink(self):
        '''
        Moves the item down in order
        of the tree
        '''
        pass

    def xchange(self, a, b):
        '''
        Exchanges a with b
        '''
        a, b = b, a
        return self
