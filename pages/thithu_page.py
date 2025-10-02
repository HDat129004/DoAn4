from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ThiThuPage(BasePage):
    BTN_VAO_THI = (By.XPATH, "//div[@class='box-content']//span[contains(text(),'Vào Thi')]")
    BTN_BAT_DAU = (By.ID, "modalStartExamBtn")
    ANSWERS = (By.CSS_SELECTOR, "label.answer")
    BTN_TIEP = (By.ID, "topNextBtn")
    BTN_KET_THUC = (By.ID, "bottomEndExamBtn")
    MODAL_SETUP = (By.ID, "setupModal")
    RESULT_MESSAGE = (By.ID, "resultMessage")
    def vao_thi(self):
        self.scroll_to_element(self.BTN_VAO_THI)
        self.wait.until(EC.element_to_be_clickable(self.BTN_VAO_THI)).click()

    def bat_dau_thi(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.BTN_BAT_DAU))
        self.driver.execute_script("arguments[0].click();", btn)
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_SETUP))
        self.wait.until(EC.visibility_of_all_elements_located(self.ANSWERS))

    def chon_dap_an(self, index=1):
        self.wait.until(EC.invisibility_of_element_located(self.MODAL_SETUP))
        answers = self.driver.find_elements(*self.ANSWERS)
        if 0 < index <= len(answers):
            self.driver.execute_script("arguments[0].scrollIntoView(true);", answers[index-1])
            self.wait.until(EC.element_to_be_clickable(answers[index-1])).click()

    def cau_tiep(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_TIEP)).click()

    def ket_thuc(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_KET_THUC)).click()

    def get_ket_qua(self):
        """Trả về thông báo kết quả"""
        return self.wait.until(EC.visibility_of_element_located(self.RESULT_MESSAGE)).text
