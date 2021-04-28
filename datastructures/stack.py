'''
Stack

Uses the LIFO, Last In First Out concept

NOTE:
In the implenetation of using a stack using a linkedlist,
remember that when the stack is initialised, it will be
initialised only with a `head` pointer, which points to `None`
Only after the 1st element is added, the `head` will point to the
1st element
'''
class StackUsingLinkedList:

    class Node:
        def __init__(self, e, nxt=None):
            self.elem = e
            self.next = nxt


    def __init__(self):
        self.head = None    # head is a pointer, NOT a `Node` itself
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        if not self.is_empty():
            s = self.head
            tr = ''
            while s != None:
                tr += str(s.elem) + '->'
                s = s.next
            return tr + 'None'
        return '[None]'

    def is_empty(self):
        return self.size == 0

    def push(self, e):
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
        else:
            n.next = self.head
            self.head = n

        self.size += 1
        return self

    def pop(self):
        '''
        Returns the most recent element added to the linked list

        Returns
        -------
        Node
            the most recently added node
        '''
        if not self.is_empty():
            t = self.head
            self.head = self.head.next
            self.size -= 1
            return t.elem
        return None
