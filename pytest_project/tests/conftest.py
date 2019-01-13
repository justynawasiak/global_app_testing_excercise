import pytest
from selenium import webdriver


@pytest.fixture
def get_driver(request):
    """
    Fixture to initiate and closing driver.
    """
    #driver = webdriver.Chrome('driver/chromedriver.exe') #local
    driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME, command_executor='http://selenium:4444/wd/hub')
    request.cls.driver = driver
    driver.maximize_window()
    yield driver
    driver.close()



