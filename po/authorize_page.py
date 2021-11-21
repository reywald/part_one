from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AuthorizePage(BasePage):
    """ The authorize app page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "Authorize TestApp"
        self.badge = self.driver.find_element(By.ID, "prompt-logo-center")
        self.heading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#prompt-logo-center + h1")

        self.user_avatar = self.driver.find_element(
            By.CSS_SELECTOR, "img:nth-child(1)")
        self.logo = self.driver.find_element(
            By.CSS_SELECTOR, 'img[alt="TestApp"]')
        
        self.user_greeting = self.driver.find_element(
            By.CSS_SELECTOR, "form p:first-child")
        self.affirm_message = self.driver.find_element(
            By.CSS_SELECTOR, "form p:nth-child(2)")
        self.cancel_button: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "button:nth-child(2)")
        self.accept_button: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "button:nth-child(1)")


    def validate_page(self):
        self.testclass.assertIn(
            "https://dev-thy56eqc.us.auth0.com/u/consent?", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)
        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Authorize App", self.heading.text)

        self.testclass.assertTrue(self.user_avatar.is_displayed())
        self.testclass.assertTrue(self.logo.is_displayed())

        self.testclass.assertTrue(self.user_greeting.is_displayed())
        self.testclass.assertIn(self.get_image_alt_text(), self.user_greeting)

        self.testclass.assertTrue(self.affirm_message.is_displayed())
        self.testclass.assertIn(
            "TestApp is requesting access to your dev-thy56eqc account.", self.affirm_message)

        self.testclass.assertTrue(self.cancel_button.is_displayed())
        self.testclass.assertTrue(self.accept_button.is_displayed())

    def perform_action(self):
        self.accept_button.click()

    def get_image_alt_text(self):
        return self.user_avatar.get_attribute("alt")
