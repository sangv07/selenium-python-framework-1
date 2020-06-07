import unittest

import pytest
from pages.courses.register_courses_page import RegisterCoursePage
from util.status_test import StatusTest

print(1.5)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCourseTests(unittest.TestCase):
    print(2.5)
    @pytest.fixture(autouse=True)
    def object_setup(self, oneTimeSetUp):
        print(2.75)
        self.cp = RegisterCoursePage(self.driver)
        self.st = StatusTest(self.driver)

    @pytest.mark.run(order=2)
    def test_course_page(self):
        self.cp.course_page("JavaScript")

    @pytest.mark.run(order=3)
    def test_enroll_course(self):
        self.cp.course_enroll("4401 1235 1542 5465", "0121", "445", "94555")

    @pytest.mark.run(order=4)
    def test_enrollment_verify(self):
        result_2 = self.cp.verify_enroll_failed()

        self.st.mark_final("Course Registration Validation ", result_2, " Registration Fail: ")

