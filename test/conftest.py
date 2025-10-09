import os
from utils.screenshot import take_screenshot
from utils.logger import get_logger
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


# Hook: Chụp screenshot khi test fail
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call":
        logger = get_logger()
        test_name = item.name.replace("/", "_")
        if rep.failed:
            logger.error(f"[FAIL] {test_name}")
            driver = item.funcargs.get("driver")
            if driver:
                outdir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(outdir, exist_ok=True)
                filepath = os.path.join(outdir, f"fail_{test_name}.png")
                take_screenshot(driver, filepath)
        elif rep.passed:
            logger.info(f"[PASS] {test_name}")
