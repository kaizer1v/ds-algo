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

class Node:
    def __init__(self, e, nxt=None):
        self.elem = e
        self.next = nxt


class StackUsingLinkedList(Node):

    def __init__(self):
        self.head = None    # head is a pointer, NOT a `Node` itself
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        if not self.is_empty():
            h = self.head
            tr = ''
            while h != None:
                tr += str(h.elem) + '->'
                h = h.next
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


def stack_up(items):
    '''
    Utility function to generate stacks

    Given a list of items, will
    return a stack containing these
    connected items

    Parameters
    ----------
    items : list
        list of items to be stacked up

    Returns
    -------
    StackUsingLinkedList
    '''
    s = StackUsingLinkedList()
    for i in items:
        s.push(i)
    return s
