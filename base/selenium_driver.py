import datetime
import logging
import os
from traceback import print_stack
from selenium.common.exceptions import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ex_cond
from util.custom_logs import CustomLogs

class SeleniumDriver():
    log = CustomLogs(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_tpye(self, by_type):

        if by_type == "id":
            return By.ID
        elif by_type == "class":
            return By.CLASS_NAME
        elif by_type == "name":
            return By.NAME
        elif by_type == "xpath":
            return By.XPATH
        elif by_type == "link":
            return By.LINK_TEXT
        elif by_type == "tag":
            return By.TAG_NAME
        elif by_type == "css":
            return By.CSS_SELECTOR
        else:
            print("Locator is incorrect or not found: + " + by_type)
        return False

    def get_title(self):
        ttl = self.driver.title
        return ttl

    def get_element(self, locator, by_type="xpath"):

        element = None
        try:
            byType = self.get_by_tpye(by_type)
            element = self.driver.find_element(byType, locator)
            self.log.info("get_element(): Element Found: " + locator + " and by_type Found " + by_type)
        except:
            self.log.error(
                "get_element(): Element Not Found: " + locator + " OR by_type Not Found " + by_type)
        return element

    def get_element_lst(self, locator, by_type="xpath"):
        element_lst = None
        try:
            byType = self.get_by_tpye(by_type)
            element_lst = self.driver.find_elements(byType, locator)
            self.log.info("get_element_lst(): Elements Found: " + locator + " and by_type Found " + by_type)
        except:
            self.log.error("get_element_lst(): Elements NOT Found: " + locator + " and by_type NOT Found " + by_type)

        return element_lst


    def element_present(self, locator, by_type="xpath"):
        element = None
        try:
            element = self.get_element(locator, by_type)
            if element is not None:
                self.log.info("Element present with Locator: " + locator + " by_type: " + by_type)
                return True
            else:
                self.log.error("Element is not present with Locator: " + by_type + " by_type " + by_type)
                return False
        except:
            self.log.error("Element not found: ")
            print_stack()
            return False

    def element_list_present(self, locator, by_type):
        element_lst = None
        try:
            element_lst = self.get_element_lst(locator, by_type)
            if element_lst is not None:
                self.log.info("List of Elements present with locator: " + locator + " and By_Type " + by_type)
                return True
            else:
                self.log.error("List of Elements NOT present with locator: " + locator + " and By_Type " + by_type)
                return False
        except:
            self.log.error("List of Elements NOT present with locator: " + locator + " and By_Type " + by_type)
            print_stack()
            return False

    def click_element(self, locator, by_type="xpath"):

        try:
            print("Click_Element: ")
            element = self.get_element(locator, by_type)
            element.click()
            self.log.info("click_element(): Element Found: " + locator + " and by_type Found " + by_type)
        except:
            self.log.error(
                "click_element(): Element Not Found: " + locator + " OR by_type Not Found " + by_type)

    def send_value(self, data, locator, by_type="xpath"):

        try:
            element = self.get_element(locator, by_type)
            element.send_keys(data)
            self.log.info("send_value: Value send to Locator: " + locator + " and by_type: + " + by_type)
        except:
            self.log.info("send_value: Value NOT send to Locator: " + locator + " and by_type: + " + by_type)

    def screen_shot(self):
        """
        Takes screenshot for current fail web page
        :return:
        """
        now = datetime.datetime.now()
        file_name = '{}{}{}{}{}{}{}.png'.format(now.month, now.day, now.year,
                                                now.hour, now.minute, now.second, now.microsecond)
        # absolute path = it is notated by a leading forward slash or drive label. starting from the root of the file system
        # relative path = it is notated by a lack of a leading forward slash. A relative file path is interpreted from the perspective your current working directory
        screenshot_dir = '../screenshots/'
        relative_file_path = screenshot_dir + file_name

        # current_dir is the canonicalised(?) directory where the program resides.
        current_dir = os.path.dirname(__file__)

        # destination_file is the parent directory of the directory where program resides.
        # outcome D:\Python\python_workspace\letskodeit_teachable_02\base\../screenshots/521202093554855627.png
        destination_file = os.path.join(current_dir, relative_file_path)
        destination_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot Saved to directory --> " + destination_file)
        except NotADirectoryError:
            self.log.error("Not a Directory issues: ")
            print_stack()

    def explicit_wait(self, locator, by_type="xpath", timeout="10", poll_frequency="0.5"):

        element = None
        try:
            byType = self.get_by_tpye(by_type)
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                     ElementNotVisibleException, ElementNotInteractableException,
                                                     NoSuchFrameException, ElementClickInterceptedException])
            #element = wait.until(ex_cond.visibility_of_element_located((by_type, locator)))
            element = wait.until(ex_cond.presence_of_element_located((byType, locator)))
            self.log.info("Waiting for elements: Element found ")
        except:
            self.log.error("Waiting for elements: Element Not found ")
        print(element)
        return element

    def web_scroll(self, direction="down"):
        try:
            if direction == "down":
                self.driver.execute_script("window.scrollBy(0, 1000);")
                self.log.info("Web Page able to scroll by: " + direction)
            elif direction == "up":
                self.driver.execute_script("window.scrollBy(0, -1000);")
                self.log.info("Web Page able to scroll by: " + direction)

        except:
            self.log.error("Web Page not able to scroll by: " + direction)

    def switch_iframe(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe
        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_default_frame(self):
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", by_type="xpath"):
        """
        Get value of the attribute of element
        Parameters:
            1. Required:
                1. attribute - attribute whose value to find
            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element
        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.get_element(locator=locator, by_type=by_type)
        value = element.get_attribute(attribute)
        return value

    def is_enable(self, locator, by_type="xpath", info=""):
        """
        Check if element is enabled
        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.get_element(locator, by_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disable")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled
