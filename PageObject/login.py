import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from Locators.locators import locators_login
from selenium.webdriver.common.by import By

from PageObject.base import base


class login(base):
    loginover_class = locators_login.btn_login
    signup_class = locators_login.btn_signup
    mobileNumLogin_xpath = locators_login.text_login_id
    click_extingacc_xpath = locators_login.btn_exiting_user
    password_xpath = locators_login.text_psw
    login_class = locators_login.btn_login_click
    tagnametext = locators_login.get_Tags
    acual_text="My Account"

    def __init__(self, driver):

        self.driver = driver

    def signup_(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        self.hover_to(self.loginover_class)
        self.click(self.signup_class)

    def exiting_user_(self):
        # self.driver.find_element_by_xpath(self.click_extingacc_xpath).click()
        self.click(self.click_extingacc_xpath)

    def enter_id(self):
        self.enter_text(self.mobileNumLogin_xpath, "8088539363")

    def enter_psw(self):
        self.enter_text(self.password_xpath, 'Uday@123')

    def login_(self):

        self.click(self.login_class)

    def tags_text(self):
        result = self.get_txt_of_tag(self.tagnametext)
        print(result)
        if "My Account" in result:
            print("succssfull")
        else:
            print("unsuccssfull",)
        self.driver.close()





