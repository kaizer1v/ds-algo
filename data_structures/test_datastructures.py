# import os, sys, inspect
# current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parent_dir = os.path.dirname(current_dir)
# sys.path.insert(0, parent_dir)

import unittest
from node import Node
from linkedlist import LinkedList

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
        self.assertEqual(n.elem, None)
        self.assertEqual(a.elem, 'a')
        self.assertEqual(n.next, None)
        self.assertEqual(a.next, None)

    def test_node_linking(self):
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

    def test_linkedlist(self):
        ll = LinkedList([4, 7])
        self.assertEqual(next(ll).elem, 4)
        self.assertEqual(next(ll).elem, 7)
        # self.assertRaises(StopIteration, next(ll))

    def test_linkedlist_add(self):
        ll = LinkedList([4, 7])
        ll.add(2).add(8)
        print(ll)

if __name__ == '__main__':
    unittest.main()
