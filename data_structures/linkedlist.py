'''
Linked Lists

[a] -> [b] -> [c] -> None

Elements are linked to each other
'''

from node import Node

class LinkedList(Node):

    def __init__(self, items):
        self.node_list = list(map(lambda i: Node(i), items))
        i = 0
        self.head_node = self.node_list[i]
        init_node = self.head_node
        while i != len(self.node_list) - 1:
            init_node.next = self.node_list[i + 1]
            init_node = self.node_list[i + 1]
            i += 1

    def __len__(self):
        pass

    def __repr__(self):
        if len(self.node_list) <= 1:
            return self.node_list[0]
        init_node = self.node_list[0]
        to_print = ''
        while init_node.next != None:
            to_print += str(init_node)
            init_node = init_node.next
        to_print += str(init_node) + str(init_node.next)
        return to_print

    def __iter__(self):
        '''
        The linked list data struture should be iterable
        '''
        return self

    def __next__(self):
        if self.head_node == None:
            raise StopIteration
        curr = self.head_node
        self.head_node = self.head_node.next
        return curr

    def add(self, e):
        '''
        add a node to the linked list
        '''
        new_node = Node(e)
        if self.head_node == None:
            self.head_node = new_node
            return self
        curr = self.head_node
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        return self

    def remove(self, n, ind=True):
        '''
        remove element by index provided by `ind`
        '''
        pass

    def find(self, e):
        '''
        returns
        '''
        pass
