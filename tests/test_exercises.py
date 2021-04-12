import unittest

class TestExercises(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_fibonacci(self):
        from exercises import fibonacci as fib
        pass

    def test_factorial(self):
        from exercises import factorial as f
        self.assertEqual(f.factorial(0), 1)
        self.assertEqual(f.factorial(-1), 1)
        self.assertEqual(f.factorial(5), 120)

    def test_permutation(self):
        pass

    def test_gcd(self):
        pass


if __name__ == '__main__':
    unittest.main()
