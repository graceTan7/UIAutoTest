# -*- coding: utf-8 -*-

import time

from WebCommon.setting import url
from TestCases.baseCase import BaseCase
from TestDatas import Comm_Datas
from PageObjects.Check_in_page.physical_session_PO import PhySessionPage as ps


class TestSmoke(BaseCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        new_url = url + Comm_Datas.event_url + Comm_Datas.check_in_url
        print(new_url)
        time.sleep(10)
        cls.driver.get(new_url)
        print('@@@@@')
        cls.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.refresh()

    def test_smoke(self):
        ps.turn_on(self.driver)

