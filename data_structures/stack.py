'''
This is a stack data structure. Uses the LIFO concept
'''
from node import Node

class StackUsingLinkedList(Node):

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        tr = 'None'
        p = self.head
        while p != None:
            tr += ' <- {}'.format(str(p.elem))
            p = p.next
        return tr

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.head = Node(e, self.head)
        self.size += 1
        return self

    def top(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self.head.elem

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is Empty')
        to_return = self.head.elem
        self.head = self.head.next
        self.size -= 1
        return to_return



class StackUsingList:

    def __init__(self):
        self.s = []

    def push(self, e):
        self.s.append(s)
        return self

    def pop(self):
        return self.s.pop()

    def __len__(self):
        return len(self.s)

    def __repr__(self):
        return ' -> '.join(self.s)
