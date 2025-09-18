import pytest
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")
    config.option.htmlpath = "reports/report.html"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot_path = f"reports/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            if hasattr(rep, "extra"):
                from pytest_html import extras
                rep.extra.append(extras.png(screenshot_path))
