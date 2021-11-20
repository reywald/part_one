import unittest
from selenium import webdriver
import time


# Import Page Objects
from po.home_page import HomePage
# from login_page import LoginPage
# from secure_page import SecurePage


class The_InternetTests(unittest.TestCase):


    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(executable_path="./webdrivers/chromedriver.exe")
        # self.driver = webdriver.Edge(executable_path="./webdrivers/msedgedriver.exe")
        self.driver = webdriver.Firefox(executable_path="./webdrivers/geckodriver.exe")
        self.page_url = "http://localhost:3000/"

    def tearDown(self) -> None:
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.page_url)

        home_page = HomePage(driver, self)
        home_page.validate_page(self.page_url)
        home_page.perform_action()

        
        time.sleep(5)