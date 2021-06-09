from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        self.action = ActionChains(self.driver)
        self.action.move_to_element(element).perform()

    def get_txt_of_tag(self, by_locator):
        return actually_result = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
        print(actually_result)
