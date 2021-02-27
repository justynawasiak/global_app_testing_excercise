from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    EMAIL = '//input[@name="email"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//button[@type="submit"]'
    ERROR = '//div[@class="text-danger"]'

    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, self.EMAIL)))

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(password)

    def login(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

    def error_message_visible(self):
        return True if self.driver.find_element_by_xpath(self.ERROR).is_displayed() else False
