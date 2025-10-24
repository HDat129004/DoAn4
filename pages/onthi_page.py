from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OnThiPage(BasePage):
    BTN_VAO_HOC_200 = (By.CSS_SELECTOR, "span.button-custom.color-1-2")
    SELECT_CHUYEN_MUC = (By.CSS_SELECTOR, "select.form-control")
    BTN_CAU_SAU = (By.XPATH, "//button[contains(text(),'Câu Sau')]")
    FIRST_ANSWER_OPTION = (By.XPATH, "(//label[contains(@class,'answer')])[1]")

    def vao_hoc_200(self):
        self.click(self.BTN_VAO_HOC_200)

    def chon_chuyen_muc(self, value):
        self.select_by_value(self.SELECT_CHUYEN_MUC, value)

    def chon_cau(self, so_cau):
        locator = (By.ID, f"cau{so_cau}")
        self.click(locator)
        # --- DÒNG SỬA LỖI QUAN TRỌNG ---
        # Sau khi click vào câu hỏi mới, phải chờ cho đến khi đáp án của nó xuất hiện
        self.wait.until(EC.presence_of_element_located(self.FIRST_ANSWER_OPTION))

    def chon_dap_an(self, stt):
        """Sử dụng self.click() với locator cụ thể, an toàn hơn."""
        answer_locator = (By.XPATH, f"(//label[contains(@class,'answer')])[{stt}]")
        self.click(answer_locator)

    def is_dap_an_dung(self, stt):
        locator = (By.XPATH, f"(//label[contains(@class,'answer')])[{stt}]//span[@class='answer-number-huy']")
        try:
            text = self.get_text(locator)
            return "✔️" in text
        except:
            return False

    def is_dap_an_sai(self, stt):
        locator = (By.XPATH, f"(//label[contains(@class,'answer')])[{stt}]//span[@class='answer-number-huy']")
        try:
            text = self.get_text(locator)
            return "❌" in text
        except:
            return False

    def next_cau(self):
        self.click(self.BTN_CAU_SAU)

    def get_answers(self):
        return self.driver.find_elements(By.XPATH, "//label[contains(@class,'answer')]")
