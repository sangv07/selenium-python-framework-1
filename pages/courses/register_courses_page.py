import logging
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
import util.custom_logs as log
from pages.locators import ElementLocators as elm
from selenium.webdriver.support import expected_conditions as ex_cond
from selenium.webdriver.support.wait import WebDriverWait


class RegisterCoursePage(BasePage):

    log = log.CustomLogs(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def search_course(self, course_name):
        self.send_value(course_name, elm._search_box, elm.by_name)
        self.click_element(elm._search_btn, elm.by_xpath)

    def select_course_to_enroll(self):
        self.click_element(elm._course_text, elm.by_xpath)
        self.web_scroll("down")
        self.click_element(elm._enroll_btn, elm.by_name)

    def get_card_number(self, num):
        self.driver.switch_to.frame("__privateStripeFrame12")
        self.send_value(num, elm._cc_num, elm.by_xpath)
        self.switch_default_frame()

    def get_expiration_date(self, exp):
        self.driver.switch_to.frame("__privateStripeFrame13")
        self.send_value(exp, elm._cc_exp, elm.by_name)
        self.switch_default_frame()

    def get_cvc_code(self, cvc):
        self.driver.switch_to.frame("__privateStripeFrame14")
        self.send_value(cvc, elm._cc_cvv, elm.by_name)
        self.switch_default_frame()
    def get_country_cd(self):
        country = self.driver.find_element_by_id("country_code_credit_card-cc")
        sel = Select(country)
        sel.select_by_visible_text("United States")

    def get_postal_cd(self, zip_cd):
        self.driver.switch_to.frame("__privateStripeFrame15")
        self.send_value(zip_cd, elm._postal_cd, elm.by_name)
        self.switch_default_frame()


    def check_save_card(self):
        # To find whether the checkbox element is selected or not
        check = self.get_element(elm._save_card, elm.by_id).get_attribute("checked")
        print(check)
        if check is not None:
            print("Element checked - ", check)
            self.click_element(elm._save_card, elm.by_id)
        else:
            print("Element checked - false")
            # self.login.sd.click_element(elm._save_card, elm.by_id)

    def check_term_agree(self):
        # To find whether the checkbox element is selected or not
        term = self.get_element(elm._term_agree, elm.by_id).is_selected()
        print(term)
        if term:
            print("Term Agreement not selected: ", term)
        else:
            self.click_element(elm._term_agree, elm.by_id)

    def click_enroll_btn(self):
        enroll = self.get_element(elm._submit_enroll, elm.by_id).is_enabled()
        if enroll:
            print("Enroll button clickable: ", enroll)
            self.click_element(elm._submit_enroll, elm.by_id)
        else:
            print("Enroll button is not clickable: ", enroll)

    def course_page(self, course_name):
        self.search_course(course_name)
        self.select_course_to_enroll()

    def set_credit_card_info(self, num, exp, csv, zip_cd):
        self.get_card_number(num)
        self.get_expiration_date(exp)
        self.get_cvc_code(csv)
        self.get_country_cd()
        self.get_postal_cd(zip_cd)

    def course_enroll(self, num, exp, csv, zip_cd):
        self.set_credit_card_info(num, exp, csv, zip_cd)
        self.check_save_card()
        self.check_term_agree()
        self.click_enroll_btn()

    def verify_enroll_failed(self):
        print(11)
        enroll_msg = self.explicit_wait(elm._enroll_error_msg, elm.by_xpath, 10, 0.5)
        if enroll_msg is not None:
            enroll = enroll_msg.is_displayed()
            return enroll
        else:
            self.log.error("Element is not Displayable: ")
            return False

    def screenshot(self):
        self.screen_shot()
