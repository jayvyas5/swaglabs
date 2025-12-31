from selenium.webdriver.common.by import By

from config.config import TestData
from pages.Basepage import BasePage


class CheckOutPage(BasePage):

    PRODUCT_NAME_INCART= (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICE_INCART= (By.CSS_SELECTOR, ".inventory_item_price")
    PRODUCT_CHECKOUT = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISHED_BUTTON = (By.ID, "finish")
    MASSAGE = (By.CSS_SELECTOR, ".complete-header")


    def __init__(self, driver,Actual_productname, Actual_productprice):
        super().__init__(driver)
        self.Actual_productname =Actual_productname
        self.Actual_productprice = Actual_productprice


    def verify_choosen_product(self):
        Expected_product_name = self.get_element_text(self.PRODUCT_NAME_INCART)
        Expected_product_price = self.get_element_text(self.PRODUCT_PRICE_INCART)

        assert self.Actual_productname == Expected_product_name
        assert self.Actual_productprice == Expected_product_price

    def product_checkout(self):
        self.do_click(self.PRODUCT_CHECKOUT)

    def fill_details(self,firstname , lastname, zipcode):
        self.enter_value(self.FIRST_NAME, firstname)
        self.enter_value(self.LAST_NAME, lastname)
        self.enter_value(self.ZIP_CODE, zipcode)
        self.do_click(self.CONTINUE_BUTTON)
        self.do_click(self.FINISHED_BUTTON)
        ACTUAL_MASSAGE =self.get_element_text(self.MASSAGE)
        assert TestData.EXPECTED_MASSAGE == ACTUAL_MASSAGE

    def proceed_checkout(self, firstname, lastname, zipcode):
        self.verify_choosen_product()
        self.product_checkout()
        self.fill_details(firstname, lastname, zipcode)










