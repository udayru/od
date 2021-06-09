from PageObject.base import base
from Locators.locators import cart_locators


class Cart(base):
    hover_Eelectonic = cart_locators.electron_hover
    mi_click = cart_locators.mi_link_text

    def __init__(self, driver):
        self.driver = driver

    def hover_electonic(self):
        self.click(self.hover_Eelectonic)
        self.click(self.mi_click)
