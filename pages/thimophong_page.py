import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ThiMoPhongPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    DE_1 = (By.ID, "exam1Btn")
    START_BTN = (By.ID, "startBtn")
    BODY = (By.TAG_NAME, "body")

    def open_home(self):
        self.driver.get("https://taplai.com/")
        self.driver.maximize_window()
        self.wait.until(lambda d: "taplai" in d.current_url.lower())

    def vao_thi_mophong(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 2);")
        time.sleep(1.5)

        all_boxes = self.driver.find_elements(By.XPATH,
                                              "//a[contains(@href,'thi-thu-mo-phong-120-tinh-huong-giao-thong-online.html')]")
        if not all_boxes:
            raise Exception("❌ Không tìm thấy link thi mô phỏng 120 tình huống!")

        vao_thi_btn = None
        for box in all_boxes:
            try:
                if "Thi 120 tình huống mô phỏng" in box.text:
                    vao_thi_btn = box
                    break
            except:
                continue

        if vao_thi_btn:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", vao_thi_btn)
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", vao_thi_btn)
        else:
            raise Exception("Không tìm thấy nút 'Vào Thi' trong box phù hợp!")

        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait.until(lambda d: "mo-phong" in d.current_url.lower())

    def chon_de_1(self):
        de1 = self.wait.until(EC.element_to_be_clickable(self.DE_1))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", de1)
        time.sleep(1)
        de1.click()

    def bat_dau_thi(self):
        start_btn = self.wait.until(EC.element_to_be_clickable(self.START_BTN))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", start_btn)
        time.sleep(1)
        start_btn.click()

    def nhan_space(self, so_lan, delay):
        body = self.wait.until(EC.presence_of_element_located(self.BODY))
        for lan, tg in enumerate(delay, start=1):
            tg_sleep = float(tg) + random.uniform(-0.5, 1.5)
            print(f"Lần {lan}: nhấn SPACE sau {tg_sleep:.2f}s")
            time.sleep(tg_sleep)
            body.send_keys(Keys.SPACE)

    def lay_ket_qua_popup(self):
        try:
            ket_qua = self.wait.until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//div[contains(@class,'modal-content')]//div[contains(text(),'Kết quả')]"
                    "//following::div[contains(text(),'ĐẠT') or contains(text(),'KHÔNG ĐẠT')]"
                ))
            ).text.strip()
            print(f"Kết quả bài thi: {ket_qua}")
            return ket_qua
        except Exception:
            print("Không tìm thấy popup kết quả.")
            return None
