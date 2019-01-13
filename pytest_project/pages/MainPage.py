class MainPage:
    URL = 'https://www.testerwork.com/'
    LOGIN = '//*[@id="sticky-nav-menu-item-9320"]/a'

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self):
        self.driver.find_element_by_xpath(self.LOGIN).click()



