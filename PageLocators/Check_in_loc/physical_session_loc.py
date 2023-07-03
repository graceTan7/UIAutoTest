# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 14:30
# @Author  : grace

from selenium.webdriver.common.by import By

# button loc
loc_PhySession_on = (By.XPATH, "//h6[text()='In-person Check-In']/ancestor::label//input[@type='checkbox' and @checked]/ancestor::label")
loc_PhySession_off = (By.XPATH, "//h6[text()='In-person Check-In']/ancestor::label//input[@type='checkbox' and not(@checked)]/ancestor::label")