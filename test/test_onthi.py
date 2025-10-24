import pytest, random
from pages.onthi_page import OnThiPage
from utils.logger import get_logger
from utils.reporter import Reporter
from utils.screenshot import take_screenshot

logger = get_logger()
reporter = Reporter()

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
        page.chon_cau(i)

        answers = page.get_answers()
        dap_an = random.randint(1, len(answers))
        page.chon_dap_an(dap_an)

        if page.is_dap_an_dung(dap_an):
            ket_qua = "Đúng"
        elif page.is_dap_an_sai(dap_an):
            ket_qua = "Sai"
        else:
            ket_qua = "Không xác định"

        logger.info(f"[{chuyen_muc}] Câu {i} - Chọn đáp án {dap_an} → {ket_qua}")
        reporter.add_result(i, dap_an, ket_qua)

        if i < min(start + 10 - 1, end):
            page.next_cau()
