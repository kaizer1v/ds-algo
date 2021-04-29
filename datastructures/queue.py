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
