from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class BienBaoPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_bienbao")    # locator giả định
    SEARCH_BTN = (By.ID, "btn_search")          # locator giả định
    FIRST_RESULT = (By.CSS_SELECTOR, ".bienbao-item")

    def tim_kiem_bien_bao(self, keyword):
        self.input_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BTN)

    def is_ket_qua_xuat_hien(self):
        return self.is_visible(self.FIRST_RESULT)
