# -*- coding: utf-8 -*-

import time

from TestCases.baseCase import BaseCase
from TestDatas import Comm_Datas

from PageObjects.Check_in_page.physical_session_PO import PhySessionPage as ps


class TestSmoke(BaseCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        new_url = Comm_Datas.portal_base_url + Comm_Datas.event_url + Comm_Datas.check_in_url
        time.sleep(1)
        cls1 = cls.driver.get(new_url)
        time.sleep(5)
        cls.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.refresh()

    def test_smoke(self):
        print("test smoke")
        ps(self.driver).turn_on()

