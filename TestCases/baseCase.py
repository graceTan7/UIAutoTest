#!/usr/bin/env python3

'''
enter portal
'''


import unittest
from selenium import webdriver

from WebCommon import setting
from PageObjects.Base_page import login_po
from TestDatas import Comm_Datas


class BaseCase(unittest.TestCase):
    """
    登录
    """
    driver = None

    @classmethod
    def setUpClass(cls):
        # 前置: open broswer, login
        cls.driver = webdriver.Chrome()
        cls.driver.get(setting.staging_url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        # login_po.Login(cls.driver).email_login(Comm_Datas.email, Comm_Datas.pwd)
        return cls.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

