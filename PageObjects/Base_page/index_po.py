# -*- coding: utf-8 -*-
# @Author  : grace

from WebCommon.BasePage import BasePageObjects
from PageLocators.Base_loc import index_loc
import time


class IndexPage(BasePageObjects):

    def check_user_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        self.wait_eleVisible(index_loc.profile_button, "index: user profile button")
        time.sleep(0.5)
        try:
            self.get_element(index_loc.user_hello, "index: find user name")
            return True
        except:
            return False
