#нажатие кнопки

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
#
# driver.get('https://perm.medsi.ru/')
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def test_button(driver_init):
    driver_init.get("https://perm.medsi.ru/")
    driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    found_button = driver_init.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
    found_button.click()
    text_element = driver_init.find_element(By.XPATH, "//h1[contains(text(), 'Записаться на прием')]")
    text = text_element.text
    assert text == "Записаться на прием"