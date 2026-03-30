#ввод данных в поле

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
#
# driver.get('https://perm.medsi.ru/')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def test_data_input(driver_init):
    driver_init.get('https://perm.medsi.ru/')
    driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    found_button = driver_init.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
    found_button.click()

    windows = driver_init.window_handles
    driver_init.switch_to.window(windows[1])
    found_button = driver_init.find_element(By.CSS_SELECTOR, "input.smed-input__native")
    found_button.click()
    found_button.send_keys("0123456789")
    found_button = driver_init.find_element(By.CSS_SELECTOR, "span.smed-base-button__content")
    found_button.click()
    text_element = driver_init.find_element(By.CSS_SELECTOR, "p.smed-text_body-sm")
    text = text_element.text
    assert not text == "Отправили код в СМС."




