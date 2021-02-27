from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DashboardPage:
    ACCOUNT_DROPDOWN = '//a[@id="account-dropdown"]'
    DESKTOP_BUTTON = '//button[@class="btn btn-primary style__add-device-button-margin___3-u9x"]'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.ACCOUNT_DROPDOWN)))

    def dropdown_visible(self):
        return True if self.driver.find_element_by_xpath(self.ACCOUNT_DROPDOWN) else False

    def add_desktop_device(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.DESKTOP_BUTTON)))
        self.driver.find_element_by_xpath(self.DESKTOP_BUTTON).click()
