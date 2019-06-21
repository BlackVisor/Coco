# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Entry.py
# @Author: Cheng JiangDong
# @Date  : 2019/3/30
# @Desc  : Later equals never


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class ParametrizedTestCase(unittest.TestCase):
    # 重写了TestCase的构造函数，加入了param属性
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testCaseClass, param=None):

        testLoader = unittest.TestLoader()
        testNames = testLoader.getTestCaseNames(testCaseClass)
        suite = unittest.TestSuite()
        for name in testNames:
            # 这个方法的入参是实例化后的测试类，测试类继承自unittest.TestCase, 其构造函数经过上述重写后需要两个入参
            # 将这个测试用例实例化后加入suite中,name和param对应构造函数中的两个参数
            suite.addTest(testCaseClass(name, param=param))
        return suite


class TestModel(ParametrizedTestCase):
    def test(self, param=None):
        self.path = param[1]
        self.argv = param[2]
        self.target = param[3]


if __name__ == '__main__':
    try:
        pass

    finally:
        pass

