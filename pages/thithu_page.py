from pages.home_page import HomePage
from selenium.webdriver.common.by import By
import time

def test_thi_thu(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_thithu()
    driver.find_element(By.LINK_TEXT, "Đề số 1").click()
    time.sleep(2)
    assert "Câu 1" in driver.page_source
