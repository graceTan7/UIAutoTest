# -*-encoding:utf-8-*-
# @Author  : gracetan
# @Time    : 2020/6/19 19:49
# @Introduction:
'''
main function
'''
import time
import os
import unittest
from HTMLTestRunnerNew import HTMLTestRunner
from WebCommon.dir_conf import testReport_dir
from dotenv import load_dotenv
import sys

if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 1 else 'development'
    envFile = '.env.development'
    if env == 'staging':
        envFile = '.env.staging'
    elif env == 'production':
        envFile = '.env.prodution'
    load_dotenv(envFile)

    now = time.strftime("%m%d_%H%M%S")
    filename = testReport_dir + now + 'result.html'
    # Instantiate the suite object
    suite = unittest.TestSuite()
    # Instantiate the TestLoader object
    loader = unittest.TestLoader()
    # 2、Use discover to find all the test cases in a directory
    base_dir = os.path.split(os.path.abspath(__file__))[0] + '/TestCases'
    # 3、add testcases to suite
    suite.addTests(loader.discover(base_dir, pattern='test*.py'))
    # run testcases
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Automation Report', description='Case Execution Status')
    runner.run(suite)
    fp.close()
