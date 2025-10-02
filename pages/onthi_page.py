from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class OnThiPage(BasePage):
    BTN_VAO_HOC_200 = (By.CSS_SELECTOR, "span.button-custom.color-1-2")
    SELECT_CHUYEN_MUC = (By.CSS_SELECTOR, "select.form-control")
    BTN_CAU_SAU = (By.XPATH, "//button[contains(text(),'Câu Sau')]")

    def vao_hoc_200(self):
        self.wait_and_click(self.BTN_VAO_HOC_200)

    def chon_chuyen_muc(self, value):
        self.select_by_value(self.SELECT_CHUYEN_MUC, value)

    def chon_cau(self, so_cau):
        locator = (By.ID, f"cau{so_cau}")
        self.wait_and_click(locator)

    def chon_dap_an(self, stt):
        answers = self.get_answers()
        if stt > len(answers):
            stt = len(answers)
        answers[stt - 1].click()  # index từ 0

    def is_dap_an_dung(self, stt):
        locator = (By.XPATH, f"(//label[contains(@class,'answer')])[{stt}]//span[@class='answer-number-huy']")
        text = self.get_text(locator)
        return "✔️" in text

    def is_dap_an_sai(self, stt):
        locator = (By.XPATH, f"(//label[contains(@class,'answer')])[{stt}]//span[@class='answer-number-huy']")
        text = self.get_text(locator)
        return "❌" in text

    def next_cau(self):
        self.wait_and_click(self.BTN_CAU_SAU)

    def get_answers(self):
        return self.driver.find_elements(By.XPATH, "//label[contains(@class,'answer')]")

    def wait_and_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
