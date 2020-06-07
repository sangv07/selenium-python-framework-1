import unittest
from tests.home.login_test import LoginTests
from tests.courses.register_course_test import RegisterCourseTests

# Get all Tests from the test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCourseTests)

# Create a test suite combining all test classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
