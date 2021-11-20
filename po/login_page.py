from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(BasePage):
    """ The Google Sign In page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "Sign in – Google accounts"
        self.heading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#headingText")
        self.subheading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#headingSubtext")
        self.username: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "input#identifierId")

    def validate_page(self):
        self.testclass.assertIn(
            "https://accounts.google.com/o/oauth2", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)

        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Sign in", self.heading.text)

        self.testclass.assertTrue(self.subheading.is_displayed())
        self.testclass.assertEqual("to continue to auth0.com", self.subheading.text)
        self.testclass.assertTrue(self.username.is_displayed())

    def perform_action(self):
        self.username.send_keys("iaweepingsaint")
        self.username.send_keys(Keys.RETURN)
