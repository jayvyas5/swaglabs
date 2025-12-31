import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from config.config import TestData
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=["chrome"], scope="class")
def setup(request):
    if request.param == "chrome":

        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {"profile.password_manager_enabled": False,
                                                         "credential_enable_service": False,"profile.password_manager_leak_detection": False})
        service = ChromeService(TestData.CHROME_EXECUTABLEPATH)
        driver = webdriver.Chrome(service=service, options=chrome_options)

    elif request.param == "firefox":
        service = FirefoxService(TestData.FIREFOX_EXECUTABLEPATH)
        driver = webdriver.Firefox(service=service)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')

        if (report.skipped and xfail) or (report.failed and not xfail):

            file_name = report.nodeid.replace("::", "_") + ".png"
            destination_path = os.path.join("reports", file_name)

            # ✅ class से driver लो
            driver = getattr(item.cls, "driver", None)

            if driver:
                driver.get_screenshot_as_file(destination_path)
                if file_name:
                    html = (
                        '<div><img src="%s" alt="screenshot" '
                        'style="width:304px;height:228px;" '
                        'onclick="window.open(this.src)" align="right"/></div>'
                         ) % file_name

                    extra.append(pytest_html.extras.html(html))

        report.extra = extra



