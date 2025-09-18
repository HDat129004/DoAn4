from pages.ketqua_page import KetQuaPage

def test_ketqua_display(driver):
    ketqua = KetQuaPage(driver)
    assert "Đậu" in ketqua.get_result() or "Trượt" in ketqua.get_result()
    assert "câu" in ketqua.get_score()
