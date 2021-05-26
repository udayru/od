import time

import pytest
from PageObject.login import login


class Test_login:
    def test_login(self, setup):
        self.driver = setup
        self.driver.get("https://www.flipkart.com/")
        time.sleep(3)

        self.lp=login(self.driver)

        self.lp.signup_()
        self.lp.exiting_user_()
        self.lp.enter_id()
        self.lp.enter_psw()
        self.lp.login_()
        time.sleep(10)


        self.lp.tags_text()

