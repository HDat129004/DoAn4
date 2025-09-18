from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LienHePage(BasePage):
    INPUT_NAME = (By.NAME, "your-name")
    INPUT_EMAIL = (By.NAME, "your-email")
    INPUT_PHONE = (By.NAME, "your-tel")
    INPUT_MESSAGE = (By.NAME, "your-message")
    BTN_SUBMIT = (By.CSS_SELECTOR, "input[type='submit']")
    SUCCESS_MSG = (By.CLASS_NAME, "wpcf7-response-output")

    def fill_contact_form(self, name, email, phone, message):
        self.input_text(self.INPUT_NAME, name)
        self.input_text(self.INPUT_EMAIL, email)
        self.input_text(self.INPUT_PHONE, phone)
        self.input_text(self.INPUT_MESSAGE, message)
        self.click(self.BTN_SUBMIT)

    def is_success(self):
        return self.is_visible(self.SUCCESS_MSG)
