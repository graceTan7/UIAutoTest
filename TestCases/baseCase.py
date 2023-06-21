#!/usr/bin/env python3

'''
login & select event
'''


import unittest
from selenium import webdriver

from WebCommon.setting import url
from PageObjects.Base_page import login_po
from PageObjects.Base_page import index_po
from TestDatas import Comm_Datas


class BaseCase(unittest.TestCase):
    """
    登录
    """
    driver = None

    @classmethod
    def setUpClass(cls):
        # 前置: open broswer, login
        web_url = url + Comm_Datas.web_index_url
        cls.driver = webdriver.Chrome()
        cls.driver.get(web_url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        login_po.Login(cls.driver).email_login(Comm_Datas.email, Comm_Datas.passwd)
        return cls.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

