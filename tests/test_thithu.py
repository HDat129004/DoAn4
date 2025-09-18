from pages.home_page import HomePage
from pages.thithu_page import ThiThuPage

def test_thi_thu_de_1(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_thithu()

    thi = ThiThuPage(driver)
    thi.chon_de_thi()
    assert thi.is_cau_hoi_xuat_hien()

    thi.nop_bai()
    assert thi.is_result_displayed()
