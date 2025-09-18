from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class KetQuaPage(BasePage):
    RESULT_TEXT = (By.CSS_SELECTOR, ".result-title")   # Ví dụ: "Đậu" hoặc "Trượt"
    SCORE_TEXT = (By.CSS_SELECTOR, ".score")           # hiển thị số câu đúng

    def get_result(self):
        return self.get_text(self.RESULT_TEXT)

    def get_score(self):
        return self.get_text(self.SCORE_TEXT)
