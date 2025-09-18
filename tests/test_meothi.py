from pages.home_page import HomePage
from pages.meothi_page import MeoThiPage

def test_meo_display(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_meo()

    meo = MeoThiPage(driver)
    assert meo.is_meo_loaded()
