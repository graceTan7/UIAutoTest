# -*-encoding:utf-8-*-
# @Author  : gracetan
# @Time    : 2020/6/19 19:49
# @Introduction:
'''
主函数
'''
import time
import os
import pytest
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from WebCommon.dir_conf import testReport_dir

if __name__ == '__main__':

    now = time.strftime("%m%d_%H%M%S")
    filename = testReport_dir + now + 'result.html'
    # 实例化套件对象
    s = unittest.TestSuite()
    # 实例化TestLoader对象
    loader = unittest.TestLoader()
    # 2、使用discover去找到一个目录下的所有测试用例
    # 3、使用s
    base_dir = os.path.split(os.path.abspath(__file__))[0] + '/TestCases'
    s.addTests(loader.discover(base_dir, pattern='test*.py'))
    # 运行
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Automation Report', description='Case Execution Status')
    runner.run(s)
    fp.close()
