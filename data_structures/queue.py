from node import Node

class QueueUsingLinkedList(Node):

    def __len__(self):
        return self._size

    def __repr__(self):
        tr = ''
        p = self._head
        while p != None:
            tr += '[' + str(p._elem) + ']->'
            p = p._next
        return tr

    def push(self, e):
        # push to begining
        n = self._Node(e, next=None)
        n._next = self._head
        self._head = n
        self._size += 1
        return self

    def pop_b(self):
        # pop from beginning
        tr = self._head
        self._head = self._head._next
        self._size -= 1
        return tr

    def pop(self):
        # pop from end
        if self._size <= 1:
            return self._head._elem
        tr = ''
        p = self._head
        while p._next._next != None:
            p = p._next
        tr = p._next._elem
        return tr

    def is_empty():
        return self._size == 0
