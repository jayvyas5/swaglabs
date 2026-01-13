from config.config import TestData
from pages.loginpage import LoginPage
from utilities.Basetestpage import BaseTestPage


class TestLoginPage(BaseTestPage):

    def test_loginpagetitle(self):
        loginpage = LoginPage(self.driver)
        title = loginpage.get_title(TestData.LOGINPAGE_TITLE)
        assert title == TestData.LOGINPAGE_TITLE

    def test_e2e(self):
        loginpage = LoginPage(self.driver)
        homePage = loginpage.do_login()
        checkOut = homePage.add_product_to_cart()
        checkOut.proceed_checkout()


