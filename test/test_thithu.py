import pytest
from pages.thithu_page import ThiThuPage


@pytest.mark.thithu
def test_thi_thu(driver):
    page = ThiThuPage(driver)
    page.open("https://taplai.com/")

    page.vao_thi()
    page.bat_dau_thi()

    for i in range(1, 26):
        page.chon_dap_an(1)
        if i < 25:
            page.cau_tiep()

    page.ket_thuc()
    actual_message = page.get_ket_qua()

    expected_message = "Bạn đã thi rớt"
    assert expected_message in actual_message, \
        f" Expected '{expected_message}' but got '{actual_message}'"

    print(f" Kết quả thi: {actual_message}")
