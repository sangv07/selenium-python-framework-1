import logging
import time

from base.base_page import BasePage
from pages.locators import ElementLocators as elm
import util.custom_logs as c_logs

class LoginPage(BasePage):
    print("LoginPage Class")

    log = c_logs.CustomLogs(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def verify_title(self):
        self.get_title()

    def get_login_lnk(self):
        print(elm.login_link)
        self.click_element(elm.login_link, elm.by_link)
        time.sleep(3)

    def get_email(self, email):
        self.send_value(email, elm.email_field, elm.by_id)

    def get_password(self, password):
        self.send_value(password, elm._pass_field, elm.by_id)

    def get_login_btn(self):
        self.click_element(elm._login_btn, elm.by_name)

    def login_page(self, email, password):
        self.get_login_lnk()
        self.get_email(email)
        self.get_password(password)
        self.get_login_btn()

    def verify_login(self):
        try:
            if self.element_present(elm._invalid_login):
                self.log.error("Login Failed: ")
                return False
            elif self.element_present(elm._valid_login):
                self.log.info("Login Successful: ")
                return True
            else:
                self.log.error("Not and Is_Element_Present Issues: ")
                print("Not and Is_Element_Present Issues: ")
        except:
            self.log.error("something else break down: ")
            print("something else break down: ")

    def screen_shot(self):
        self.screen_shot()
