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
    webauto测试用例基类
    包含了PageObjects当中，用到所有的selenium底层方法
    包含通用的一些元素操作，如alert,iframe,windows...
    日志记录、实现失败截图
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, loc, img_doc="", timeout=30, poll_frequency=0.5):
        """

        :param loc: 元素loc
        :param img_doc: 图片名称
        :param timeout: WebDriverWait 超时时间
        :param poll_frequency: 休眠时间的间隔（步长）时间
        :return:
        """
        logging.info("等待元素 {} 可见.".format(loc))
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except TimeoutError:
            logging.exception("等待元素可见失败！")
            self.save_web_screenshot(img_doc)
            raise TimeoutError
        else:
            end = datetime.datetime.now()
            logging.info(f"开始等待时间点：{start}，结束等待时间点：{end}，等待时长为：{end - start}")

    # 等待元素存在
    def wait_eleExists(self, loc, img_doc="", timeout=30, poll_frequency=0.5):
        '''
        :param loc: 元素loc
        :param img_doc: 图片名称
        :param timeout: WebDriverWait 超时时间
        :param poll_frequency: 休眠时间的间隔（步长）时间
        :return:
        '''
        logging.info(f"等待元素{loc}存在。")
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_all_elements_located(loc))
        except TimeoutError:
            logging.exception("等待元素存在失败！")
            self.save_web_screenshot(img_doc)
            raise TimeoutError
        else:
            # 结束等待的时间
            end = datetime.datetime.now()
            logging.info(f"开始等待时间：{start}，结束等待时间点：{end}，等待时长为：{end - start}")

    # 查找一个元素
    def get_element(self, loc, img_doc=""):
        '''

        :param loc:
        :param img_doc:
        :return:
        '''
        logging.info(f"查找{img_doc}中的元素{loc}")
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except Exception as e:
            logging.exception("查找元素fail")
            self.save_web_screenshot(img_doc)
            return False

    # 点击操作
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
        logging.info(f"点击元素 {loc}")
        try:
            ele.click()
        except:
            logging.exception("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入
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
            logging.info(f" 给元素{loc}输入文本内容：{args[0]}")
            return ele
        except:
            logging.exception("元素输入操作失败")
            self.save_web_screenshot(img_loc)
            raise

    # 获取元素属性值
    def get_element_attribute(self, loc, attr_name, img_doc, timeout=30, poll_frequency=0.5):
        self.wait_eleExists(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            attr_value = ele.get_attribute(attr_name)
        except:
            logging.exception("获取元素属性失败")
            self.save_web_screenshot(img_doc)
            raise
        else:
            logging.info(f"获取元素{loc}的属性{attr_name}值为：{attr_value}")
            return attr_value

    # 获取元素文本内容
    def get_element_text(self, loc, img_doc='', timeout=30, poll_frequency=0.5):
        self.wait_eleExists(loc, img_doc, timeout, poll_frequency)
        ele = self.get_element(loc, img_doc)
        try:
            text = ele.text
        except:
            logging.exception("获取元素文本值失败")
            self.save_web_screenshot(img_doc)
            raise
        else:
            logging.info(f"获取元素 {loc} 的文本值为：{text}")
            return text

    # 截图
    def save_web_screenshot(self, img_doc):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logging.info("网页截图成功。图片存储在：{}".format(screenshot_dir + "/" + filepath))
        except:
            logging.exception("网页截屏失败！")
