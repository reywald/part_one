from .base_page import BasePage
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class PasswordPage(BasePage):
    """ The Google Password Entry page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "Sign in – Google accounts"
        self.heading: WebElement = self.driver.find_element(
            By.ID, "headingText")
        self.account_name: WebElement = self.driver.find_eleme(By.ID, "profileIdentifier")
        self.password: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "input[type='password']")

    def validate_page(self):
        self.testclass.assertIn(
            "https://accounts.google.com/signin/v2/challenge/", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)

        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Welcome", self.heading.text)

        self.testclass.assertTrue(self.account_name.is_displayed())
        self.testclass.assertTrue(os.getenv("ACCOUNT_NAME"), self.account_name.text)

        self.testclass.assertTrue(self.password.is_displayed())

    def perform_action(self):
        self.password.send_keys(os.getenv("ACCOUNT_PASSWORD"))
        self.password.send_keys(Keys.RETURN)
