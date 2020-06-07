import time

import pytest
import unittest

from ddt import ddt, data, unpack
from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursePage
from util.status_test import StatusTest

print(1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginDataTests(unittest.TestCase):
    print(2)

    @pytest.fixture(autouse=True)
    def class_set_up(self, oneTimeSetUp):
        print(3)
        self.lp = LoginPage(self.driver)
        self.cp = RegisterCoursePage(self.driver)
        self.st = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    @data(("test@email.com", "abcabc"))
    @unpack
    def test_login_verify(self, email, password):
        print(4)
        self.lp.login_page(email, password)
        print(5)
        result_1 = self.lp.verify_login()
        if result_1:
            self.st.mark(result_1, "Login Successful: ")
        else:
            self.st.mark(result_1, "Login Un-Successful: ")

        # self.st.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[4]/a/img").click()
        # self.st.driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[4]/ul/li[5]/a").click()
        # time.sleep(3)

    @pytest.mark.run(order=2)
    @data(['JavaScript'])
    @unpack
    def test_course_page(self, course_name):
        self.cp.course_page(course_name)

    @pytest.mark.run(order=3)
    @data(("4401 1235 1542 5465", "0121", "445", "94555"), ("4401 4465 4525 5465", "0122", "225", "87179"))
    @unpack
    def test_enroll_course(self, num, exp, csv, zip_cd):
        self.cp.course_enroll(num, exp, csv, zip_cd)

    @pytest.mark.run(order=4)
    def test_enrollment_verify(self):
        result_2 = self.cp.verify_enroll_failed()

        self.st.mark_final("Course Registration Validation ", result_2, " Registration Fail: ")

