import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_linkedlist(self):
        self.assertEqual(LinkedList([]), [])
        self.assertNotEqual(LinkedList([1, 2, 3]), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
