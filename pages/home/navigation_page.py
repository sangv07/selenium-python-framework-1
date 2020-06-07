import logging

import util.custom_logs as c_logs
from base.base_page import BasePage
from pages.locators import ElementLocators as elm

class NavigationPage(BasePage):

    log = c_logs.CustomLogs(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def nav_all_course(self):
        self.click_element(elm._all_course, elm.by_link)

    def nav_my_course(self):
        self.click_element(elm._my_course, elm.by_link)

    def nav_to_practice(self):
        self.click_element(elm._to_practice, elm.by_link)

    def nav_to_setting(self):
        self.click_element(elm._to_setting, elm.by_class)

    def nav_to_home(self):
        self.click_element(elm._home_logo, elm.by_xpath)

    def sign_out(self):
        self.nav_to_setting()
        self.click_element(elm._log_out, elm.by_link)

