from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import utils.config as config

class HomePage(BasePage):
    MENU_ONTHI = (By.LINK_TEXT, "Ôn thi GPLX")
    MENU_THITHU = (By.LINK_TEXT, "Thi thử GPLX")
    MENU_BIENBAO = (By.LINK_TEXT, "Biển báo")
    MENU_MEO = (By.LINK_TEXT, "Mẹo thi")
    MENU_LIENHE = (By.LINK_TEXT, "Liên hệ")

    def open_home(self):
        self.open(config.BASE_URL)

    def go_to_onthi(self):
        self.click(self.MENU_ONTHI)

    def go_to_thithu(self):
        self.click(self.MENU_THITHU)

    def go_to_bienbao(self):
        self.click(self.MENU_BIENBAO)

    def go_to_meo(self):
        self.click(self.MENU_MEO)

    def go_to_lienhe(self):
        self.click(self.MENU_LIENHE)
