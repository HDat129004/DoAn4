from pages.home_page import HomePage
from pages.onthi_page import OnThiPage

def test_onthi_A1(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_onthi()

    onthi = OnThiPage(driver)
    onthi.chon_hang_A1()
    assert onthi.is_first_question_displayed()
