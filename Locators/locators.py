from selenium import webdriver
from selenium.webdriver.common.by import By


class locators_login:
    btn_login = (By.CLASS_NAME, "_1_3w1N")
    btn_signup = (By.CLASS_NAME, "_2HFOTA")
    btn_exiting_user = (By.XPATH, "//span[text()='Existing User? Log in']")
    text_login_id = (By.XPATH, "//input[@class='_2IX_2- VJZDxU']")
    text_psw = (By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']")
    btn_login_click = (By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
    get_text_user = (By.CLASS_NAME,'exehdJ')

class cart_locators:
    electron_hover =(By.CLASS_NAME,"_2I9KP_")
    mi_link_text=(By.LINK_TEXT,"Mi")
