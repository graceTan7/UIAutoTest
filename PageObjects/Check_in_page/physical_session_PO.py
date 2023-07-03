# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 14:26
# @Author  : grace

from WebCommon.BasePage import BasePageObjects
from PageLocators.Check_in_loc import physical_session_loc as ps_loc


class PhySessionPage(BasePageObjects):

    def turn_on(self):
        """turn on physical check-in button"""
        self.wait_eleExists(ps_loc.loc_PhySession_off)
        self.get_element(ps_loc.loc_PhySession_off)
        self.click_element(ps_loc.loc_PhySession_off)

    def turn_off(self):
        """turn off physical check-in button"""
        self.get_element(ps_loc.loc_PhySession_on)
        self.click_element(ps_loc.loc_PhySession_on)

    def check_phy_session_exist():
        pass
