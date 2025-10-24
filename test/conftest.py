import os
import pytest
from selenium import webdriver
from utils.logger import get_logger

# This import is needed for pytest-html.
# It will raise an error if pytest-html is not installed.
from pytest_html import extras

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment to run in headless mode
    driver = webdriver.Chrome(options=options)
    driver.get("https://taplai.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        logger = get_logger()
        test_name = item.name.replace("/", "_")
        if report.passed:
            logger.info(f"[PASS] {test_name}")
        elif report.failed:
            logger.error(f"[FAIL] {test_name}")

        # --- Screenshot for HTML Report on failure ---
        if report.failed:
            try:
                driver = item.funcargs['driver']
                screenshot_dir = os.path.join(os.getcwd(), "screenshots")
                os.makedirs(screenshot_dir, exist_ok=True)
                screenshot_path = os.path.join(screenshot_dir, f"fail_{item.name.replace('::', '_').replace('/', '_')}.png")
                driver.save_screenshot(screenshot_path)
                extra.append(extras.image(screenshot_path))
            except Exception as e:
                print(f"Failed to take screenshot: {e}")
    
    report.extra = extra

def pytest_html_report_title(report):
    """Customizes the report title."""
    report.title = "Báo cáo kiểm thử tự động"
