from .base_page import BasePage
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class AccountPage(BasePage):
    """ The Google Sign In page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "Sign in – Google accounts"
        self.heading: WebElement = self.driver.find_element(
            By.ID, "headingText")
        self.subheading: WebElement = self.driver.find_element(
            By.ID, "headingSubtext")
        self.username: WebElement = self.driver.find_element(
            By.ID, "identifierId")

    def validate_page(self):
        self.testclass.assertIn(
            "https://accounts.google.com/o/oauth2/v2/auth/", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)

        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Sign in", self.heading.text)

        self.testclass.assertTrue(self.subheading.is_displayed())
        self.testclass.assertIn(
            "to continue to ", self.subheading.text)
        self.testclass.assertTrue(self.username.is_displayed())

    def perform_action(self):
        self.username.send_keys(os.getenv("ACCOUNT_USER"))
        self.username.send_keys(Keys.RETURN)
