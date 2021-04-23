'''
Linked Lists

[a] -> [b] -> [c] -> None

Multiple nodes are linked to each other
'''

from node import Node

class LinkedList(Node):

    def __init__(self, items):
        i = 0
        while i + 1 != len(items):
            self.join(items[i], items[i + 1])
            i = i + 1
        self.join(items[i], None)

    def join(self, a, b):
        if not type(a) == Node:
            a = Node(a)
        if not type(b) == Node:
            b = Node(b)
        a.next = b
        return self

    def __repr__(self):
        return ''


class LinkedListIterable:

  def insert(self, n_data):
    node = Node(n_data, self.head)
    self.head = node

  def find(self, n_data):
    node = self.head
    while node.get_next() != None:
      if node.get_data() == n_data:
        return True
      node = node.get_next()
    return node.get_data() == n_data

  def print(self):
    node = self.head
    while node.get_next() != None:
      print(node.get_data())
      node = node.get_next()
    if node.get_next() == None:
      print(node.get_data())

  def is_empty(self):
    return self.head == None

  def __iter__(self):
    return self

  def __next__(self):
    if self.head == None:
      raise StopIteration
    node = self.head
    self.head = node.get_next()
    return node.get_data()

  def __init__(self):
    self.head = None
