import unittest
from sort_insertion import sort_insertion

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


if __name__ == '__main__':
    unittest.main()
