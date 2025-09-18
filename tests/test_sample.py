import pytest
from selenium import webdriver
from pages.base_page import BasePage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_open_google(driver):
    page = BasePage(driver)
    page.open('https://www.google.com')
    assert 'Google' in driver.title
