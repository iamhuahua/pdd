# -*- coding:utf-8 -*-
import unittest
from normal_test.test_mathfunction import TestMathFunction

if __name__ == '__main__':
    suit = unittest.TestSuite()
    tests = [TestMathFunction("test_add"), TestMathFunction("test_minus"), TestMathFunction("test_multiply"),
             TestMathFunction("test_divide")]
    suit.addTests(tests)
    with open('UnittestTextReport.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suit)
