from unittest import TestCase
from abc import abstractmethod
from selenium import webdriver


class BasePage:
    """ The base page from which other page objects inherit"""

    def __init__(self, driver: webdriver, testclass: TestCase) -> None:
        """Assign elements to the page members"""
        self.driver = driver
        self.testclass = testclass

    @abstractmethod
    def validate_page(self):
        """ Check that all elements of the page are in place with
        the right text content
        """
        pass

    @abstractmethod
    def perform_action(self, *args):
        """Perform the page's prescribe action or actions."""
        pass
