import time
import pytest

from base.web_driver_factory import WebDriverFactory

print(2.5)
@pytest.fixture()
def setUp():
    print("Runs BEFORE every method: SetUP**")
    yield
    print("\nRuns AFTER every method: TearDown**")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("************OneTime SetUp BEFORE Test Class**************")
    web_dr = WebDriverFactory(browser)
    driver = web_dr.get_webdriver_instance()
    time.sleep(3)

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    time.sleep(10)
    #driver.quit()
    print("***********OneTime TearDown AFTER Test Class*************")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
