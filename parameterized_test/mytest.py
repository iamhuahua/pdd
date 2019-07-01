# -*- coding:utf-8 -*-

import unittest
import nose_parameterized
from tool import DataToParam


def calcu(a, b):
    res = a + b
    return res


data = DataToParam().text('../files/test.txt')
# print data
# print ('data type is %s' % (type(data)))


class MyTest(unittest.TestCase):
    """参数化，自动的运行list里边的数据"""

    @nose_parameterized.parameterized.expand(data)
    def test2(self, x, y, z):

        z = int(z)
        res = calcu(int(x), int(y))
        self.assertEqual(res, z)


if __name__ == '__main__':
    unittest.main()
