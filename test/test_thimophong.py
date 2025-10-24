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

    for idx, delay in enumerate(delay_list, start=1):
        page.nhan_space(so_lan=1, delay=[delay])
        diem = page.lay_diem_cau(idx)

        assert diem is not None, f" Câu {idx}: Không lấy được điểm. Chức năng hiển thị điểm bị lỗi."


        print(f"Câu {idx}: {diem} điểm")