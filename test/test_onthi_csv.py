import pytest, csv
from pages.onthi_page import OnThiPage
from utils.logger import get_logger
from utils.reporter import Reporter
from utils.screenshot import take_screenshot

logger = get_logger()
reporter = Reporter()

# Load đáp án từ CSV
def load_answers(filepath="C:/Users/Admin/Desktop/DoAn4/dap_an.csv"):
    answers = {}
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            answers[int(row["so_cau"])] = int(row["dap_an"])
    return answers

DAP_AN = load_answers()

# Danh sách chuyên mục và khoảng câu hỏi
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

    # Test 10 câu đầu (hoặc ít hơn nếu không đủ)
    for i in range(start, min(start + 10, end + 1)):
        page.chon_cau(i)

        dap_an = DAP_AN.get(i)
        assert dap_an, f"Không tìm thấy đáp án cho câu {i}"

        # Chọn đáp án đúng từ file
        page.chon_dap_an(dap_an)

        if page.is_dap_an_dung(dap_an):
            ket_qua = "Đúng"
        else:
            ket_qua = "Sai"
            take_screenshot(driver, f"{chuyen_muc}_cau_{i}")

        logger.info(f"[{chuyen_muc}] Câu {i} - Đáp án {dap_an} → {ket_qua}")
        reporter.add_result(i, dap_an, ket_qua)

        # Chuyển sang câu tiếp theo nếu chưa phải câu cuối test
        if i < min(start + 10 - 1, end):
            page.next_cau()
