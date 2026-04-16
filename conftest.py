import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver_init():
    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# @pytest.fixture(scope='function')
# def browser(request):
#     a = request.param
#     if a == 'Chrome':
#         chrom = webdriver.Chrome()
#         chrom.maximize_window()
#         chrom.implicitly_wait(10)
#         yield chrom
#         chrom.quit()
#     elif a == 'Firefox':
#         firefox = webdriver.Firefox()
#         firefox.maximize_window()
#         firefox.implicitly_wait(10)
#         yield firefox
#         firefox.quit()
#     elif a == 'Safari':
#         safari = webdriver.Safari()
#         safari.maximize_window()
#         safari.implicitly_wait(10)
#         yield safari
#         safari.quit()