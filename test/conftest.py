import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # nếu muốn chạy ẩn
    driver = webdriver.Chrome(options=options)
    driver.get("https://taplai.com/")
    yield driver
    driver.quit()
