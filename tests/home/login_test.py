import pytest
import unittest

from pages.courses.register_courses_page import RegisterCoursePage
from pages.home.login_page import LoginPage
from util.status_test import StatusTest

print(1)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    print(2)

    @pytest.fixture(autouse=True)
    def class_set_up(self, oneTimeSetUp):
        print(3)
        self.lp = LoginPage(self.driver)
        self.cp = RegisterCoursePage(self.driver)
        self.st = StatusTest(self.driver)

    @pytest.mark.run(order=1)
    def test_login_verify(self):
        print(4)
        self.lp.login_page("test@email.com", "abcabc")
        print(5)
        result_1 = self.lp.verify_login()
        if result_1:
            self.st.mark(result_1, "Login Successful: ")
        else:
            self.st.mark(result_1, "Login Un-Successful: ")

    # @pytest.mark.run(order=2)
    # def test_course_page(self):
    #     self.cp.course_page("JavaScript")
    #
    # @pytest.mark.run(order=3)
    # def test_enroll_course(self):
    #     self.cp.course_enroll("4401 1235 1542 5465", "0121", "445", "94568")
    #
    # @pytest.mark.run(order=4)
    # def test_enrollment_verify(self):
    #     result_2 = self.cp.verify_enroll_failed()
    #
    #     self.st.mark_final("Course Registration Validation ", result_2, " Registration Fail: ")

