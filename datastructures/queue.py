'''
Queue

A datastructure that uses the FIFO concept i.e First In First Out
'''
class QueueUsingLinkedList:

    class Node:
        def __init__(self, e, nxt=None):
            self.elem = e
            self.next = nxt


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
        n = self.Node(e)
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



