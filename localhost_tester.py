import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


# Import Page Objects
from po.home_page import HomePage
from po.login_page import LoginPage


class LocalhostTesterm(unittest.TestCase):

    def setUp(self) -> None:
        self.set_chrome_driver()
        self.page_url = "http://localhost:3000/"

    def tearDown(self) -> None:
        # self.driver.quit()
        pass

    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.page_url)

        home_page = HomePage(driver, self)
        home_page.validate_page(self.page_url)
        home_page.perform_action()

        login_page = LoginPage(driver, self)
        login_page.validate_page()
        login_page.perform_action()

        time.sleep(500)

    def set_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discovery")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--user-agent=DN")

        self.driver = webdriver.Chrome(
            executable_path="./webdrivers/chromedriver.exe", options=chrome_options)
        self.driver.delete_all_cookies()
