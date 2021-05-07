import unittest
from peak_finder import peak_1d

class TestExercises(unittest.TestCase):

    def test_peak_1d(self):
        self.assertEqual(peak_1d([0]), 0)
        self.assertEqual(peak_1d([0, 0, 0]), 0)
        self.assertEqual(peak_1d([-5, 4, 2, 9, 7]), 4)
        self.assertEqual(peak_1d([1, 2, 3, 4, 5]), 5)
        self.assertEqual(peak_1d([5, 4, 3, 2, 1]), 5)

if __name__ == '__main__':
    unittest.main()
