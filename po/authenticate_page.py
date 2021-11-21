from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class AuthenticatedPage(BasePage):
    """ The Authenticated page"""

    def __init__(self, driver, testclass) -> None:
        """Assign elements to the page members"""
        super().__init__(driver, testclass)

        self.page_url = self.driver.current_url
        self.page_title = "React App"
        self.heading: WebElement = self.driver.find_element(
            By.CSS_SELECTOR, "#root .App-header > h1")
        
        self.avatar = self.driver.find_element(By.CLASS_NAME, "Avatar")
        self.first_name = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(3)")
        self.last_name = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(4)")

    def validate_page(self, fname, lname):
        self.testclass.assertEqual(
            "http://localhost:3000/authenticated?login=e30=#", self.page_url)
        self.testclass.assertEqual(self.page_title, self.driver.title)
        self.testclass.assertTrue(self.heading.is_displayed())
        self.testclass.assertEqual("Howdy, you're now Authenticated", self.heading.text)

        self.testclass.assertTrue(self.avatar.is_displayed())
        self.testclass.assertEqual(f"{fname} {lname}", self.avatar.get_attribute("alt"))

        self.testclass.assertEqual(f"First Name: {fname}", self.first_name.text)
        self.testclass.assertEqual(f"Last Name: {lname}", self.last_name.text)

    def perform_action(self):
        self.login_button.click()
