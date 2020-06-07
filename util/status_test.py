import logging
from traceback import print_stack

import util.custom_logs as c_log
from base.base_page import BasePage

class StatusTest(BasePage):

    log = c_log.CustomLogs(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.result_list = []

    def result_set(self, result, result_msg):
        print(result)
        print(result_msg)
        try:
            if result is not None:
                if result:
                    self.result_list.append("**PASS**")
                    self.log.info("##### 1 Verification Successful: and " + result_msg)
                else:
                    self.result_list.append("***FAIL***")
                    self.log.error("#### 2 Verification Failed: and " + result_msg)
            # elif result:
            #     self.result_list.append("**PASS**")
            #     self.log.info("##### Verification Successful: and " + result_msg)
            else:
                self.result_list.append("***FAIL***")
                self.log.error("#### 3 Verification Failed: " + result_msg)
        except:
            self.result_list.append("***FAIL***")
            self.log.error("#### 4 Verification Failed: " + result_msg)
            print("#### Verification Failed: " + result_msg)
            print_stack()

    def mark(self, result, result_msg):
        """
        Mark the result of the verification point in a test case
        """
        self.result_set(result, result_msg)


    def mark_final(self, test_name, result, result_msg):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.result_set(result, result_msg)
        print(self.result_list)

        if "***FAIL***" in self.result_list:
            self.log.error(test_name + " -->> Test Failed: ")
            self.result_list.clear()
            assert True == False
        else:
            self.log.info(test_name + "-->> Test Pass Successfully: ")
            self.result_list.clear()
            assert True == True
