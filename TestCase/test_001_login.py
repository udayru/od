import time

import console as console
from selenium import webdriver
import pytest
from PageObject.login import login
from PageObject.add_to_cart import Cart


class Test_login:
    def test_login(self, setup):
        self.driver = setup
        self.driver.get("https://www.flipkart.com/")
        time.sleep(10)

        self.lp = login(self.driver)

        self.lp.signup_()
        # self.lp.exiting_user_()
        self.lp.enter_id()
        self.lp.enter_psw()
        self.lp.login_()
        print("hello")
        self.ac = Cart(self.driver)
        time.sleep(10)
        self.ac.hover_electonic()

    def test_goo(self, setup):
        self.driver = setup
        self.driver.get(
            "https://www.google.com/search?q=goog&oq=goog&aqs=chrome..69i57j69i59l2j0i67i131i433i457j69i60l3j69i65.1293j0j7&sourceid=chrome&ie=UTF-8")
