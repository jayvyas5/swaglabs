from selenium.webdriver.common.by import By

from config.config import TestData
from pages.Basepage import BasePage
from pages.Homepage import HomePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    LOGINPAGE_TITLE = (By.CSS_SELECTOR, ".login-title")

    """constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """page actions"""
    def get_loginPage_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.enter_value(self.USERNAME, username)
        self.enter_value(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)




