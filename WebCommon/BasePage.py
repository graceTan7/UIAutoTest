# -*- coding: utf-8 -*-
# @Author  : gracetan

import datetime
import logging
import time

from WebCommon.dir_conf import screenshot_dir
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObjects:
    """
    webauto test case base class
    Contains all the selenium underlying methods used in PageObjects
    Includes some common element operations, such as alert, iframe, windows...
    Log record, realize failure screenshot
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # wait for element visible
    def wait_eleVisible(self, loc, img_doc="", timeout=30, poll_frequency=0.5):
        """

        :param loc: element loc
        :param img_doc: image name
        :param timeout: WebDriverWait timeout
        :param poll_frequency: sleep time interval (step) time
        :return:
        """
        logging.info("Waiting for element {} to be visible.".format(loc))
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except TimeoutError:
            logging.exception("Failed to wait element to be visible!")
            self.save_web_screenshot(img_doc)
            raise TimeoutError
        else:
            end = datetime.datetime.now()
            logging.info(f"Start waiting time: {start}, end waiting time: {end}, waiting time is: {end - start}")

    # wait for element exist
    def wait_eleExists(self, loc, img_doc="", timeout=30, poll_frequency=0.5):
        '''
        :param loc: Element location
        :param img_doc: Image name
        :param timeout: WebDriverWait timeout
        :param poll_frequency: Sleep time interval (step length) time
        :return:
        '''
        logging.info(f"Wait for element {loc} to exist.")
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_all_elements_located(loc))
        except TimeoutError:
            logging.exception("Waiting for element to exist failed!")
            self.save_web_screenshot(img_doc)
            raise TimeoutError
        else:
            # End time to wait
            end = datetime.datetime.now()
            logging.info(f"Start waiting time: {start}, end waiting time point: {end}, waiting time is: {end - start}")

    # get element
    def get_element(self, loc, img_doc=""):
        '''

        :param loc:
        :param img_doc:
        :return:
        '''
        logging.info(f"Find element {loc} in {img_doc}")
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except Exception as e:
            logging.exception("failed to find element")
            self.save_web_screenshot(img_doc)
            return False

    # click
    def click_element(self, loc, img_doc="", timeout=30, poll_frequency=0.5):
        '''

        :param loc:
        :param img_doc:
        :param timeout:
        :param poll_frequency:
        :return:
        '''
        self.wait_eleVisible(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.element_to_be_clickable(loc))
        logging.info(f"Click element {loc}")
        try:
            ele.click()
        except:
            logging.exception("Click element failed")
            self.save_web_screenshot(img_doc)
            raise

    def input_text(self, loc, *args):
        """

        :param loc:
        :param args:
        :return:
        """
        img_loc = ""
        timeout = 30
        poll_frequency = 0.5
        self.wait_eleVisible(loc, img_loc, timeout, poll_frequency)
        ele = self.get_element(loc, img_loc)
        try:
            ele.send_keys(args[0])
            logging.info(f"Enter text content {args[0]} for element {loc}")
            return ele
        except:
            logging.exception("Element input operation failed", loc)
            self.save_web_screenshot(img_loc)
            raise

    def get_element_attribute(self, loc, attr_name, img_doc, timeout=30, poll_frequency=0.5):
        self.wait_eleExists(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            logging.exception("Failed to get element attribute")
            self.save_web_screenshot(img_doc)
            raise
        else:
            logging.info(f"Get the attribute {attr_name} value of element {loc} as: {attr_value}")
            return attr_value

    def get_element_text(self, loc, img_doc='', timeout=30, poll_frequency=0.5):
        self.wait_eleExists(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            text = ele.text
        except:
            logging.exception("Failed to get element text value")
            self.save_web_screenshot(img_doc)
            raise
        else:
            logging.info(f"Get the text value of element {loc} as: {text}")
            return text

    def save_web_screenshot(self, img_doc):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("Screenshot successful. The picture is stored in:{}".format(screenshot_dir + "/" + filepath))
        except:
            logging.exception("Failed to take screenshot of webpage!")
