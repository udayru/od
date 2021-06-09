import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Firefox(executable_path="/home/uk/browers/firefox/geckodriver")
    return driver
    yield

    driver.quit()
