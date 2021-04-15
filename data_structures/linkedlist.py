'''
Linked Lists

*-> [a] -> [b] -> [c] ->*

Elements are linked to each other
'''

from node import Node

class LinkedList:

    def __init__(self, items):
        if len(items) == 0 or items == None:
            return Node(None)

        node_list = list(map(lambda i: Node(i), items))
        head = Node()
        for i, n in enumerate(node_list):
            if i == 0:
                head.next = node_list[i]
            elif i == len(node_list) - 2:
                node_list[i].next = node_list[i + 1]
                node_list[i + 1].next = None
            else:
                node_list[i].next = node_list[i + 1]

    def __repr__(self):
        pass

    def __iter__(self):
        '''
        The linked list data struture should be iterable
        '''
        pass

    def __next__(self):
        pass

    def head(self):
        '''
        Get the head node of the linked list
        '''
        pass

    def tail(self):
        '''
        Get the tail node of the linked list
        '''
        pass

ll = LinkedList([1, 5, 2])
