from pages.home_page import HomePage
from selenium.webdriver.common.by import By

def test_mo_onthi(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_onthi()
    assert "Ôn thi GPLX" in driver.page_source

def test_chon_bo_de(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_onthi()
    driver.find_element(By.LINK_TEXT, "200 câu hỏi A1").click()
    assert "Câu 1" in driver.page_source
