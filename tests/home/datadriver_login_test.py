import time

import pytest
import unittest

from ddt import ddt, data, unpack
from pages.home.login_page import LoginPage
from pages.courses.register_courses_page import RegisterCoursePage
from pages.home.navigation_page import NavigationPage
from util.status_test import StatusTest
from util.read_data import get_csv_data

print(1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginDataDrivenCSVTests(unittest.TestCase):
    print(2)

    @pytest.fixture(autouse=True)
    def class_set_up(self, oneTimeSetUp):
        print(3)
        self.lp = LoginPage(self.driver)
        self.cp = RegisterCoursePage(self.driver)
        self.st = StatusTest(self.driver)
        self.np = NavigationPage(self.driver)

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
    @data(*get_csv_data("D:\\Python\\python_workspace\\letskodeit_teachable_02\\test_data.csv"))
    @unpack
    def test_course_page(self, course_name, num, exp, csv, zip_cd):
        self.cp.course_page(course_name)

    @pytest.mark.run(order=3)
    @data(*get_csv_data("D:\\Python\\python_workspace\\letskodeit_teachable_02\\test_data.csv"))
    @unpack
    def test_enroll_course(self, course_name, num, exp, csv, zip_cd):
        self.cp.course_enroll(num, exp, csv, zip_cd)

        self.np.nav_to_home()
        self.np.sign_out()

        self.driver.quit()

    # @pytest.mark.run(order=4)
    # def test_enrollment_verify(self):
    #     result_2 = self.cp.verify_enroll_failed()
    #     self.st.mark_final("Course Registration Validation ", result_2, " Registration Fail: ")
