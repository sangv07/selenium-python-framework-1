from base.selenium_driver import SeleniumDriver
from base.web_driver_factory import WebDriverFactory

class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
