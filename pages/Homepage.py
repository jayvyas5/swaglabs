from selenium.webdriver.common.by import By
from pages.Basepage import BasePage
from pages.checkOutPage import CheckOutPage


class HomePage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, "a[id='item_3_title_link'] div[class='inventory_item_name ']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1)")
    PRODUCT= (By.XPATH, "//div[normalize-space()='Test.allTheThings() T-Shirt (Red)']")
    ADD_TO_CART_BTN = (By.ID, "add-to-cart")
    CART_BUTTON = (By.CSS_SELECTOR, ".shopping_cart_link")


    """constructor"""
    def __init__(self, driver):
        super().__init__(driver)


    def product_details(self):
        Actual_productname = self.get_element_text(self.PRODUCT_NAME)
        Actual_Productprice = self.get_element_text(self.PRODUCT_PRICE)
        return Actual_productname, Actual_Productprice

    def product_selection(self):
        self.do_click(self.PRODUCT)

    def add_to_cart(self):
        self.do_click(self.ADD_TO_CART_BTN)

    def click_cart_button(self):
        self.do_click(self.CART_BUTTON)

    def add_product_to_cart(self):
        Actual_productname, Actual_Productprice = self.product_details()
        self.product_selection()
        self.add_to_cart()
        self.click_cart_button()
        return CheckOutPage(self.driver,Actual_productname,Actual_Productprice)


