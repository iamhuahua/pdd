# -*- coding:utf-8 -*-
import unittest
import nose_parameterized


def calcu(a, b):
    res = a + b
    return res


data = [
    [1, 2, 3],
    [0, 0, 0],
    [999, 1, 1000]
]

print ('data type is %s' % (type(data)))


class MyTest(unittest.TestCase):
    """参数化，自动的运行list里边的数据"""

    @nose_parameterized.parameterized.expand(data)
    def test1(self, a, b, c):
        res = calcu(a, b)
        self.assertEqual(res, c)


if __name__ == '__main__':
    unittest.main()
