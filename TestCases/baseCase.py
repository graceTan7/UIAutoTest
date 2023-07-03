#!/usr/bin/env python3

'''
enter portal
'''


import unittest
from selenium import webdriver

from PageObjects.Base_page import login_po
from TestDatas import Comm_Datas


class BaseCase(unittest.TestCase):
  """
  login
  """
  driver = None

  @classmethod
  def setUpClass(cls):
    # precondition: open broswer, login
    cls.driver = webdriver.Chrome()
    print(Comm_Datas.portal_base_url)
    cls.driver.get(Comm_Datas.portal_base_url)
    cls.driver.maximize_window()
    cls.driver.implicitly_wait(5)
    login_po.Login(cls.driver).email_login(Comm_Datas.email, Comm_Datas.pwd)
    return cls.driver

  @classmethod
  def tearDownClass(cls):
    cls.driver.quit()

