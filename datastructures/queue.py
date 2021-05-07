'''
Queue

A datastructure that uses the FIFO concept i.e First In First Out

NOTE:
In the implenetations of using a queue (both using LL as well as lists),
remember that when the queue is initialised, it will be
initialised with a `head` and a `tail` pointers, which points to `None`
i.e. the same element. Only after the 1st element is added, the `head`
will point to the 1st element, so will the `tail`. From the 2nd element
onwards, the `tail` will always point to the "earliest" element added
to the queue where as the `head` will always point to the most "recent"
element added to the queue

REMEMBER:
HEAD -> Most Recent
TAIL -> Most Earliest
'''
class Node:
    def __init__(self, e, nxt=None):
        self.elem = e
        self.next = nxt


class QueueUsingLinkedList(Node):

    def __init__(self):
        self.head = None    # points to most recently added elem
        self.tail = None    # points to most earliest added elem
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        if not self.is_empty():
            s = self.tail
            tr = ''
            while s != None:
                tr += str(s.elem) + '->'
                s = s.next
            return tr + 'None'
        return '[None]'

    def is_empty(self):
        return self.size == 0

    def enqueue(self, e):
        '''
        Creates a new node & adds to beginning of the linked list

        Parameters
        ----------
        e : str, int
            the content/value of the new node

        Returns
        -------
        self
        '''
        n = Node(e)
        if self.is_empty():
            self.head = n
            self.tail = n
        else:
            self.head.next = n
            self.head = n
        self.size += 1
        return self

    def dequeue(self):
        '''
        Returns the most earliest element added to the linked list

        Returns
        -------
        Node
            the most recently added node
        '''
        tr = self.tail.elem
        self.tail = self.tail.next
        self.size -= 1
        return tr



class RandomisedQueue(QueueUsingLinkedList):
    '''
    A randomised queue is where an item from the
    queue is removed at random
    '''
    from random import randint

    def __init__(self):
        super(RandomisedQueue, self).__init__()

    def dequeue(self):
        '''
        Remove an item at random

        Returns
        -------
        Node
            a node selected at random
        '''
        pass

def queue_up(items):
    '''
    Utility function to generate queue

    Given a list of items, will
    return a queue containing these
    connected items

    Parameters
    ----------
    items : list
        list of items to be queued up

    Returns
    -------
    QueueUsingLinkedList
    '''
    q = QueueUsingLinkedList()
    for i in items:
        q.enqueue(i)
    return q



class QueueUsingList:

    def __init__(self):
        self.q = []

    def enqueue(self, e):
        self.q.append(e)

    def dequeue(self):
        if len(self.q) != 0:
            return self.q[-1]
        return None



class PriorityQueue:
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
    def __init__(self):


class DoubleEndedQueue:
    '''
    Double Ended Queue

    You can insert and remove from both
    the ends of a queue. This data structure has been
    implemented using an inbuilt list datastructure
    '''

    def __init__(self):
        self.dq = []

    def __repr__(self):
        return ' <-> '.join(self.dq)

    def __len__(self):
        return len(self.dq)

    def lpush(self, e):
        self.dq = [e] + self.dq
        return self

    def rpush(self, e):
        self.dq.append(e)
        return self

    def lpop(self):
        # Remove from the left
        tr = self.dq[0]
        self.dq = self.dq[1:]
        return tr

    def rpop(self):
        # Remove from the left
        tr = self.dq[-1]
        self.dq = self.dq[:-1]
        return tr
