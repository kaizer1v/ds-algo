# import os, sys, inspect
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

import unittest
from node import Node, NodeLR
# from linkedlist import LinkedList
from stack import StackUsingLinkedList
from queue import QueueUsingLinkedList
from matrix import Matrix

class TestNode(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @classmethod
    def tearDownClass(self):
        pass

    def setUp(self):
        n = Node()
        a = Node('a')
        b = Node('b')
        c = Node('c')

    def tearDown(self):
        pass

    def test_node(self):
        self.assertEqual(n.elem, None)
        self.assertEqual(a.elem, 'a')
        self.assertEqual(n.next, None)
        self.assertEqual(a.next, None)

    def test_node_linking(self):
        a.next = b
        b.next = c

        self.assertEqual(a.next, b)
        self.assertEqual(b.next, c)
        self.assertEqual(c.next, None)
        self.assertEqual(a.next.next, c)
        self.assertEqual(a.next.next.next, None)

    def test_node_lr(self):
        a = NodeLR('a')
        b = NodeLR('b')
        c = NodeLR('c')
        a.next = b
        b.prev = a
        b.next = c
        c.prev = b
        print(a, b, c)

# class TestLinkedList(unittest.TestCase):

#     def setUp(self):
#         self.ll = LinkedList([4, 7])

#     def tearDown(self):
#         pass

#     def test_linkedlist(self):
#         self.assertEqual(next(self.ll).elem, 4)
#         self.assertEqual(next(self.ll).elem, 7)
#         # self.assertRaises(StopIteration, next(self.ll))

#     def test_linkedlist_add(self):
#         self.assertEqual(len(self.ll), 2)
#         self.ll.add(2).add(8)
#         self.assertEqual(len(self.ll), 4)

    # def test_linkedlist_remove(self):
    #     self.ll.remove(1)       # remove elem on index `1`
    #     self.assertEqual(len(self.ll), 1)


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = StackUsingLinkedList()
        self.assertEqual(len(s), 0)
        self.assertEqual(s._head, None)
        s.push(3).push(9).push(4)
        self.assertEqual(len(s), 3)
        self.assertEqual(s._head, 4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(len(s), 2)

# class TestMatrix(unittest.TestCase):
#     def test_validity(self):
#         # m1 = Matrix([1, 2])
#         # print(m1)
#         m2 = Matrix([[1, 2, 3], [3, 2, 1]])
#         print(m2)
#         # self.assertFalse(m)

if __name__ == '__main__':
    unittest.main()
