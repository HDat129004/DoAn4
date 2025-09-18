from pages.home_page import HomePage
from pages.bienbao_page import BienBaoPage

def test_search_bienbao(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_bienbao()

    bienbao = BienBaoPage(driver)
    bienbao.tim_kiem_bien_bao("Stop")
    assert bienbao.is_ket_qua_xuat_hien()
