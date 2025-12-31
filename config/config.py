import os


class TestData:
    CHROME_EXECUTABLEPATH = "/Users/beraagi/Documents/chromedriver-mac-arm64/chromedriver"
    FIREFOX_EXECUTABLEPATH = "/Users/beraagi/Documents/geckodriver"

    BASE_URL = "https://www.saucedemo.com/"

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_FILE_PATH = os.path.join(BASE_DIR, "reports", "automation.log")

    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    LOGINPAGE_TITLE = "Swag Labs"

    FIRST_NAME = "JOHNY"
    LAST_NAME = "DEPP"
    ZIP_CODE = "0102030"

    EXPECTED_MASSAGE = "Thank you for your order!"