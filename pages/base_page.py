import os
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ========= CORE =========
    def open(self, url):
        """Mở URL"""
        self.driver.get(url)

    def click(self, locator):
        """Click vào phần tử"""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text, clear_first=True):
        """Nhập text vào ô input"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        if clear_first:
            el.clear()
        el.send_keys(text)

    def get_text(self, locator):
        """Lấy text của element"""
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator, timeout=5):
        """Check element hiển thị"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except:
            return False

    def is_present(self, locator, timeout=5):
        """Check element có trong DOM"""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False

    # ========= SELECT =========
    def select_by_value(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_value(value)

    def select_by_index(self, locator, index):
        Select(self.driver.find_element(*locator)).select_by_index(index)

    def select_by_visible_text(self, locator, text):
        Select(self.driver.find_element(*locator)).select_by_visible_text(text)

    # ========= ADVANCED ACTIONS =========
    def hover(self, locator):
        """Di chuột vào element"""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        """Double click"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).double_click(element).perform()

    def right_click(self, locator):
        """Right click"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).context_click(element).perform()

    def press_key(self, locator, key=Keys.ENTER):
        """Nhấn phím (Enter, ESC,...) trên element"""
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.send_keys(key)

    def scroll_to_element(self, locator):
        """Cuộn tới element"""
        el = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", el)

    def scroll_by(self, x=0, y=300):
        """Cuộn theo toạ độ"""
        self.driver.execute_script(f"window.scrollBy({x},{y});")

    # ========= BACKWARD COMPATIBILITY =========
    def scroll_to(self, locator):
        """Alias cho scroll_to_element để test cũ không bị lỗi"""
        return self.scroll_to_element(locator)

    def wait_for(self, locator, timeout=10):
        """Chờ element xuất hiện (cho test cũ)"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    # ========= UTILS =========
    def take_screenshot(self, filename="screenshot.png"):
        """Chụp màn hình"""
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, filename)
        self.driver.save_screenshot(path)
        return path

    def get_attribute(self, locator, attr):
        """Lấy attribute"""
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.get_attribute(attr)

    def get_current_url(self):
        """Lấy URL hiện tại"""
        return self.driver.current_url

    def get_title(self):
        """Lấy title hiện tại"""
        return self.driver.title
