import pytest
from pages.onthi_page import OnThiPage
from utils.logger import get_logger
from utils.reporter import Reporter
from utils.datadriven import read_csv

logger = get_logger()
reporter = Reporter()

DAP_AN = read_csv("data/dap_an.csv")

CHUYEN_MUC = [
    ("khai-niem", 1, 100),
    ("van-hoa", 101, 110),
    ("ky-thuat", 111, 125),
    ("bien-bao", 126, 215),
    ("tinh-huong", 216, 250),
]

@pytest.mark.parametrize("chuyen_muc, start, end", CHUYEN_MUC)
def test_onthi_chuyen_muc(driver, chuyen_muc, start, end):
    page = OnThiPage(driver)
    page.vao_hoc_200()
    page.chon_chuyen_muc(chuyen_muc)

    for i in range(start, min(start + 10, end + 1)):
        row = next((r for r in DAP_AN if int(r["so_cau"]) == i), None)
        assert row, f"Không tìm thấy đáp án cho câu {i}"
        dap_an = int(row["dap_an"])

        page.chon_cau(i)
        page.chon_dap_an(dap_an)

        ket_qua = "Đúng" if page.is_dap_an_dung(dap_an) else "Sai"
        logger.info(f"[{chuyen_muc}] Câu {i} - Đáp án {dap_an} → {ket_qua}")
        reporter.add_result(i, dap_an, ket_qua)

        if i < min(start + 9, end):
            page.next_cau()
