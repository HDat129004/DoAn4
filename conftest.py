import pytest
from utils.driver_factory import get_driver
import utils.config as config

@pytest.fixture
def driver():
    driver = get_driver(config.BROWSER)
    yield driver
    driver.quit()
