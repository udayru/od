from selenium import webdriver
from selenium.webdriver.common.by import By


class locators_login:
    btn_login = (By.CLASS_NAME, "_3Ep39l")
    btn_signup = (By.CLASS_NAME, "_2HFOTA")
    btn_exiting_user = (By.XPATH, "//span[text()='Existing User? Log in']")
    text_login_id = (By.XPATH, "//input[@class='_2zrpKA _1dBPDZ']")
    text_psw = (By.XPATH, "//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
    btn_login_click = (By.XPATH, "//button[@class='_2AkmmA _1LctnI _7UHT_c']")
    get_Tags=(By.TAG_NAME, "body")