# import os, sys, inspect
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

import unittest
from node import Node, NodeLR
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
        pass

    def tearDown(self):
        pass

    def test_node(self):
        n = Node()
        a = Node('a')
        b = Node('b')
        c = Node('c')
        self.assertEqual(n.elem, None)
        self.assertEqual(a.elem, 'a')
        self.assertEqual(n.next, None)
        self.assertEqual(a.next, None)

    def test_node_linking(self):
        n = Node()
        a = Node('a')
        b = Node('b')
        c = Node('c')

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


class TestStack(unittest.TestCase):

    def test_stack(self):
        s = StackUsingLinkedList()
        self.assertEqual(len(s), 0)
        self.assertEqual(s.head, None)
        # 3 <- 9 <- 4
        s.push(3).push(9).push(4)
        self.assertEqual(len(s), 3)
        # self.assertEqual(s.head, 4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(len(s), 2)


class TestQueue(unittest.TestCase):

    def test_queue(self):
    q = QueueUsingLinkedList()
    q.enqueue(9).enqueue(4).enqueue(3)
    self.assertEqual(len(q), 3)
    self.assertEqual(q.head, 3)
    self.assertEqual(q.tail, 9)
    self.assertEqual(q.dequeue(), 9)
    self.assertEqual(len(q), 2)
    q.enqueue(7)
    self.assertEqual(q.dequeue(), 4)

if __name__ == '__main__':
    unittest.main()
