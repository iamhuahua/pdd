# -*- coding:utf-8 -*-

import os
import mock
import unittest


class Remove(object):
    def rmdir(self, path='/Users/dgg/Downloads/log'):
        r = os.rmdir(path)
        if r == None:
            return 'success'
        else:
            return 'fail'

    def exists_get_rmdir(self):
        return self.rmdir()


class MockTest(unittest.TestCase):
    def setUp(self):
        self.r = Remove()

    def tearDown(self):
        pass

    def test_success_rmdir(self):
        """
        删除目录成功
        :return:
        """
        success_path = mock.Mock(return_value='success')
        print success_path
        self.r.rmdir = success_path
        self.assertEqual(self.r.exists_get_rmdir(), 'success')

    def test_fail_rmdir(self):
        """
        删除目录失败
        :return:
        """
        fail_path = mock.Mock(return_value='fail')
        print fail_path
        self.r.rmdir = fail_path
        self.assertEqual(self.r.exists_get_rmdir(), 'fail')


if __name__ == '__main__':
    unittest.main(verbosity=2)
