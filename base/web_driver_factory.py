"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        Returns:
          None
        """
        self.browser = browser

    """
        Set chrome driver and iexplorer environment based on OS
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def get_webdriver_instance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
           'WebDriver Instance'
        """

        url = "https://letskodeit.teachable.com/"
        if self.browser == 'chrome':
            chrome_opt = webdriver.ChromeOptions()
            chrome_opt.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_opt)
        elif self.browser =='ff':
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Ie

        driver.implicitly_wait(2)
        driver.get(url)
        print(driver.current_url)

        return driver
