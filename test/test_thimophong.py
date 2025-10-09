import pytest
from pages.thimophong_page import ThiMoPhongPage
from utils.datadriven import read_excel

@pytest.mark.usefixtures("driver")
def test_thi_mophong_space(driver):
    page = ThiMoPhongPage(driver)
    data = read_excel("data\\data_mophong.xlsx", sheet_name="Sheet1")
    delay_list = [float(row["thoi_gian"]) for row in data if row.get("thoi_gian")]

    page.open_home()
    page.vao_thi_mophong()
    page.chon_de_1()
    page.bat_dau_thi()
    page.nhan_space(so_lan=len(delay_list), delay=delay_list)

    ket_qua_thuc_te = page.lay_ket_qua_popup()
    expected = "KHÔNG ĐẠT"

    assert ket_qua_thuc_te == expected, (
        f"Kết quả sai! Mong đợi: {expected}, Thực tế: {ket_qua_thuc_te}"
    )
    print(f" Hoàn thành bài thi mô phỏng. Kết quả: {ket_qua_thuc_te}")
