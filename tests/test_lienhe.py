from pages.home_page import HomePage
from pages.lienhe_page import LienHePage

def test_gui_lienhe_thanh_cong(driver):
    home = HomePage(driver)
    home.open_home()
    home.go_to_lienhe()

    lienhe = LienHePage(driver)
    lienhe.fill_contact_form(
        name="Nguyen Van A",
        email="a@example.com",
        phone="0912345678",
        message="Tôi muốn được tư vấn thêm về thi GPLX"
    )

    assert lienhe.is_success(), "Thông báo gửi liên hệ không hiển thị"
