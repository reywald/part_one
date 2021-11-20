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
        self.page_title = "Sign in - Google Accounts"
        self.heading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, ".main .banner h1")
        self.subheading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "h2.hidden-small")
        self.username: WebElement = self.driver.find_element(By.ID, "Email")
        self.submit: WebElement = self.driver.find_element(By.ID, "next")

    def validate_page(self):
        self.testclass.assertIn(
            "https://accounts.google.com/ServiceLogin?continue=", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)

        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual(
            "One account. All of Google.", self.heading.text)

        self.testclass.assertTrue(self.subheading.is_displayed())
        self.testclass.assertIn(
            "Sign in with your Google Account", self.subheading.text)
        self.testclass.assertTrue(self.username.is_displayed())

    def perform_action(self):
        self.username.send_keys("iaweepingsaint")
        self.username.send_keys(Keys.RETURN)
