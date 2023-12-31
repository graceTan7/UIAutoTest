# -*-encoding:utf-8-*-

"""
login testcases
"""
import unittest
from ddt import ddt, data
from selenium import webdriver

from PageObjects.Base_page import login_po
from PageObjects.Base_page import index_po
from TestDatas import Comm_Datas
from TestDatas import login_data as ld
from TestCases.baseCase import BaseCase


@ddt
class TestLogin(BaseCase):
    """
    initial login
    """

    driver = None

    def tearDown(self):
        self.driver.refresh()

    def test_smoke(self):
        pass
        # login_po.Login(self.driver).email_login(Comm_Datas.email, Comm_Datas.pwd)
        # assert index_po.IndexPage(self.driver).check_user_name_exists()

    # @data(*ld.wrong_datas)
    # def test_login_0_failed_by_wrong_datas(self, data):
    #     print('------', data)
    #     login_po.Login(self.driver).email_login(data["email"], data["passwd"])
    #     assert data["check"] == login_po.Login(self.driver).get_error_msg_from_loginForm()
    #
    # @data(*ld.fail_datas)
    # def test_login_1_failed_by_fail_datas(self, data):
    #     login_po.Login(self.driver).email_login(data["email"], data["passwd"])
    #     assert data["check"] == login_po.Login(self.driver).get_error_msg_popup()
