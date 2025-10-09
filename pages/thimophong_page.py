import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ThiMoPhongPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    MENU_THI = (By.XPATH, "//span[contains(text(),'Thi 120 tình huống')]")
    BTN_VAO_THI = (By.XPATH, "//a[contains(@href,'thi-thu-mo-phong')]//span[contains(text(),'Vào Thi')]")
    DE_1 = (By.ID, "exam1Btn")
    BTN_BAT_DAU = (By.ID, "startBtn")
    BTN_SPACE = (By.ID, "spaceBtn")
    POPUP_KQ = (By.XPATH, "//div[contains(@class,'modal-content')]//div[contains(text(),'Kết quả')]/following::div[1]")

    def open_home(self):
        self.driver.get("https://taplai.com/")
        self.driver.maximize_window()
        time.sleep(2)

    def vao_thi_mophong(self):
        vao_thi = self.wait.until(EC.element_to_be_clickable(self.BTN_VAO_THI))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", vao_thi)
        time.sleep(1)
        vao_thi.click()
        time.sleep(2)

    def chon_de_1(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.DE_1))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
        time.sleep(1)
        btn.click()

    def bat_dau_thi(self):
        start = self.wait.until(EC.element_to_be_clickable(self.BTN_BAT_DAU))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start)
        time.sleep(1)
        start.click()

    def nhan_space(self, so_lan=10, delay=None):
        body = self.driver.find_element(By.TAG_NAME, "body")
        delay = delay or [2] * so_lan
        for i, tg in enumerate(delay, 1):
            print(f"→ Lần {i}: bấm SPACE sau {tg}s")
            time.sleep(float(tg))
            body.send_keys(Keys.SPACE)

    def lay_ket_qua_popup(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        # Đợi thêm vài giây để trang hiển thị popup
        print("⏳ Đang chờ popup kết quả hiển thị...")
        time.sleep(7)

        wait = WebDriverWait(self.driver, 20)
        try:
            ket_qua = wait.until(EC.visibility_of_element_located((
                By.XPATH,
                "//div[contains(@class,'modal-content')]//div[contains(text(),'Kết quả')]//following::div[contains(text(),'ĐẠT') or contains(text(),'KHÔNG ĐẠT')]"
            ))).text.strip()
            print(f" Kết quả bài thi: {ket_qua}")
            return ket_qua
        except Exception as e:
            print(f" Không tìm thấy popup kết quả. Chi tiết lỗi: {e}")
            return None
    def lay_diem_cau(self, so_cau):
        try:
            time_id = f"time{so_cau}"
            td = self.driver.find_element(By.ID, time_id)
            value = td.text.strip()
            score = int(value) if value.isdigit() else 0
            print(f"→ Câu {so_cau}: điểm = {score}")
            return score
        except Exception:
            print(f"⚠️ Không tìm thấy kết quả cho câu {so_cau}")
            return 0
