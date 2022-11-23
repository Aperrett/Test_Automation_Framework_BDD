from lib.webdriver.page import BrowserPage
from selenium.webdriver.common.by import By


class BasicChecks(BrowserPage):
    def input_field_by_id(self, id, text_value):
        driver = self.context.driver
        driver.find_element(By.ID, id).send_keys(text_value)

    def click_submit_button(self):
        driver = self.context.driver
        driver.find_element(By.ID, 'submitContact').click()
