import pytest
import time
from pages.mophong_page import MoPhongPage

@pytest.mark.mophong
def test_hoc_mo_phong(driver):
    page = MoPhongPage(driver)
    page.open("https://taplai.com/")
    time.sleep(5)
    page.vao_hoc()
    try:
        page.bat_dau()
    except:
        pass
    page.play_video()
    actual_time = page.cho_va_bam_space(expected_time=10.88, tol=0.5)
    print(f"✅ Space click thành công tại {actual_time:.2f}s (mong đợi ~10.88s)")
