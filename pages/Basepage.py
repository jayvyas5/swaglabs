from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.loggerUtil import LoggerUtil


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        LoggerUtil.getLogger().info("{} {}".format("Actions Click Element ", by_locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_value(self, by_locator, text):
        LoggerUtil.getLogger().info("{} {}".format("Enter Value", by_locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        LoggerUtil.getLogger().info("{} {}".format("Get Element Text", by_locator))
        element =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_element_present(self, by_locator):
        element =WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        LoggerUtil.getLogger().info("{} {}".format("Get Page Title", title))
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def handle_alert(self, by_locator):
        LoggerUtil.getLogger().info("{} {}".format("JavaScript Executor Click Element", by_locator))
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()


