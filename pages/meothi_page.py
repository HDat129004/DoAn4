from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MeoThiPage(BasePage):
    MEO_LIST = (By.CSS_SELECTOR, ".meo-item")   # cần chỉnh lại locator thật

    def is_meo_loaded(self):
        return self.is_visible(self.MEO_LIST)

