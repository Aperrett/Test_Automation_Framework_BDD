import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BrowserPage:
    __DEFAULT_TIMEOUT = 60

    def __init__(self, context):
        self.context = context

    def h1_is(self, text):
        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), text)
            )

            return True
        except TimeoutException:
            return False

    def h2_is(self, text):
        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'h2'), text)
            )

            return True
        except TimeoutException:
            return False

    def th_is(self, text):
        try:
            WebDriverWait(
                self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.text_to_be_present_in_element((By.TAG_NAME, 'th'), text)
            )

            return True
        except TimeoutException:
            return False

    def title_is(self, text):
        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.title_is(text))

            return True
        except TimeoutException:
            return False

    def title_contains(self, text):
        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.title_contains(text))

            return True
        except TimeoutException:
            return False

    def url_is(self, text):
        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.url_to_be(text))

            return True
        except TimeoutException:
            return False

    def url_starts_with(self, prefix):
        pattern = '^' + re.escape(prefix)

        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.url_matches(pattern))

            return True
        except TimeoutException:
            return False

    def url_ends_with(self, suffix):
        pattern = re.escape(suffix) + '$'

        try:
            WebDriverWait(self.context.driver, self.__DEFAULT_TIMEOUT).until(
                EC.url_matches(pattern))

            return True
        except TimeoutException:
            return False

    def visit(self, url):
        self.context.driver.get(url)
