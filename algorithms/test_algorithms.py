import unittest
from sort_insertion import sort_insertion
from sort_selection import sort_selection
from sort_merge import sort_merge

class TestAlgorighms(unittest.TestCase):

    def test_sort_insertion(self):
        a = [9, -8, 0, 4]
        b = ['z', 'd', 'a']
        c = [{
            'name': 'bxl',
            'num': 35
        }, {
            'name': 'azm',
            'num': 88
        }, {
            'name': 'ggg',
            'num': -85
        }]

        self.assertEqual(sort_insertion(a), [-8, 0, 4, 9])
        self.assertEqual(sort_insertion(b), ['a', 'd', 'z'])
        self.assertEqual(sort_insertion(c, key='num'), [{
                                                            'name': 'ggg',
                                                            'num': -85
                                                        }, {
                                                            'name': 'bxl',
                                                            'num': 35
                                                        }, {
                                                            'name': 'azm',
                                                            'num': 88
                                                        }]
        )

    def test_sort_selection(self):
        a = []
        b = [0]
        c = [2, 3, 1]
        self.assertEqual(sort_selection(a), [])
        self.assertEqual(sort_selection(b), [0])
        self.assertEqual(sort_selection(c), [1, 2, 3])
        self.assertEqual(sort_selection(c, asc=False), [3, 2, 1])

    def test_sort_merge(self):
        a = []
        b = [0]
        c = [2, 5, 3, 1, 6, 4]
        self.assertEqual(sort_merge(a), [])
        self.assertEqual(sort_merge(b), [0])
        self.assertEqual(sort_merge(c), [1, 2, 3, 4, 5, 6])


if __name__ == '__main__':
    unittest.main()
