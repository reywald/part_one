from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import unittest


# Import Page Objects
from po.home_page import HomePage
from po.account_page import AccountPage
from po.authorize_page import AuthorizationPage
from po.authenticate_page import AuthenticatedPage
from po.password_page import PasswordPage


class LocalhostTesterm(unittest.TestCase):

    def setUp(self) -> None:
        load_dotenv()
        # self.set_firefox_driver()
        self.set_chrome_driver()
        self.page_url = os.getenv("WEB_URL")

    def tearDown(self) -> None:
        self.driver.quit()
        # pass

    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.page_url)

        # Navigate to the homepage
        home_page = HomePage(driver, self)
        home_page.validate_page(self.page_url)
        home_page.perform_action()

        # Gmail user account page
        account_page = AccountPage(driver, self)
        account_page.validate_page()
        account_page.perform_action()

        # Script called to enter password for gmail account
        # Unfortunately google detects automated sign in
        # and refuses this page to load
        # pass_page = PasswordPage(driver, self)
        # pass_page.validate_page()
        # pass_page.perform_action()

        # Script to validate TestApp authorization
        authorize_page = AuthorizationPage(driver, self)
        authorize_page.validate_page()
        authorize_page.perform_action()
        fname, lname = authorize_page.get_image_alt_text()

        # Validate that the image shows and the user name is displayed.
        auth_page = AuthenticatedPage(driver, self)
        auth_page.validate_page()
        auth_page.perform_action(fname, lname)

        time.sleep(5)

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

    def set_firefox_driver(self):
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

        profile = webdriver.FirefoxProfile(
            os.getenv("APPDATA") + os.getenv("FIREFOX_PROFILE"))
        profile.set_preference("dom.webdriver.enabled", False)
        profile.set_preference("useAutomationExtension", False)
        profile.update_preferences()

        self.driver = webdriver.Firefox(executable_path="./webdrivers/geckodriver.exe",
                                        firefox_profile=profile, desired_capabilities=DesiredCapabilities.FIREFOX)
