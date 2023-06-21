# -*-encoding:utf-8-*-
# @Author  : gracetan
# @Time    : 2020/7/7 10:37
# @Introduction: 日志模块配置
import logging
from logging.handlers import RotatingFileHandler
import os
import time

from WebCommon import dir_conf

ft = " %(asctime)s %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
dataft = " %a, %d %b %Y %H:%M:%S "
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())
# 将日志同时输出到屏幕和日志文件
handler_1 = logging.StreamHandler()

print(dir_conf.testLog_dir)
# 日志回滚
handler_2 = RotatingFileHandler(dir_conf.testLog_dir + "/Auto_{0}.log".format(curTime),backupCount=20,encoding="utf-8")
handler_2 = RotatingFileHandler(dir_conf.testLog_dir + "/Auto_{0}.log".format(curTime), backupCount=20,encoding="utf-8")
# 设置root logger
logging.basicConfig(format=ft, datefmt=dataft, level=logging.INFO, handlers=[handler_1, handler_2])
