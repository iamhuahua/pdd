# -*- coding:utf-8 -*-
import unittest
from normal_test.mathfunction import *

"""test mathfunction"""


class TestMathFunction(unittest.TestCase):
    """test method add(a,b)"""

    def test_add(self):
        self.assertEqual(3, add(1, 2))

    """test method minus(a,b)"""

    def test_minus(self):
        self.assertEqual(-1, minus(1, 2))

    """test method multiply(a,b)"""

    def test_multiply(self):
        self.assertEqual(6, multiply(3, 2))

    """test method divide(a,b)"""
    @unittest.skip("I don't want to run this case")
    def test_divide(self):
        self.assertEqual(2.5, divide(5, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
