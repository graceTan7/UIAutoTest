# -*-encoding:utf-8-*-
# @Author  : gracetan
# @Time    : 2020/7/7 11:06
# @Introduction: 框架路径，测试路径

import os

# 框架顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# 测试用例路径
testCase_dir = os.path.join(base_dir, "CD_TestCases")
# 测试数据路径
testData_dir = os.path.join(base_dir, "TestDatas")
# 测试报告路径
testReport_dir = os.path.join(base_dir, "OutPuts/Reports/")
# 日志输出路径
testLog_dir = os.path.join(base_dir, "OutPuts/Logs")
# 截图输出路径
screenshot_dir = os.path.join(base_dir, "OutPuts/Screenshots")


