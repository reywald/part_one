from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HomePage(BasePage):
    """ The home page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "React App"
        self.heading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#root .App-header > h1")
        self.login_button: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#root p a")

    def validate_page(self, url: str):
        self.testclass.assertEqual(url, self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)
        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Welcome to Dashboard", self.heading.text)
        self.testclass.assertTrue(self.login_button.is_displayed())

    def perform_action(self):
        # self.login_button.click()
        self.driver.get("https://accounts.google.com/o/oauth2/v2/auth/oauthchooseaccount?redirect_uri=https%3A%2F%2Fdevelopers.google.com%2Foauthplayground&prompt=consent&response_type=code&client_id=407408718192.apps.googleusercontent.com&scope=email&access_type=offline&flowName=GeneralOAuthFlow")
