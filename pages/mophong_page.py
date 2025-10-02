from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage

class MoPhongPage(BasePage):
    BTN_VAO_HOC = (By.XPATH, "//a[contains(@href,'thi-thu-mo-phong')]//span[contains(text(),'Vào Học')]")
    BTN_BAT_DAU = (By.ID, "startButton")
    BTN_PLAY = (By.ID, "playPauseButton")
    BTN_SPACE = (By.ID, "spaceButton")
    TIME_DISPLAY = (By.ID, "timeDisplay")

    def vao_hoc(self):
        self.scroll_to_element(self.BTN_VAO_HOC)
        self.wait.until(EC.element_to_be_clickable(self.BTN_VAO_HOC)).click()

    def bat_dau(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_BAT_DAU)).click()

    def play_video(self):
        self.wait.until(EC.element_to_be_clickable(self.BTN_PLAY)).click()

    def cho_va_bam_space(self, expected_time: float, tol: float = 0.5):
        time.sleep(max(0, expected_time - 0.3))
        self.scroll_to_element(self.BTN_SPACE)
        self.wait.until(EC.element_to_be_clickable(self.BTN_SPACE)).click()
        displayed = self.wait.until(EC.visibility_of_element_located(self.TIME_DISPLAY)).text
        actual_time = float(displayed.replace("Time: ", "").replace("s", "").strip())
        assert abs(actual_time - expected_time) <= tol, f"❌ Expected ~{expected_time}s but got {actual_time}s"
        return actual_time
