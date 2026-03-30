import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_init():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()