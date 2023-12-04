# test_mymath.py

import unittest
from mymath import add, subtract

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = subtract(7, 3)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()