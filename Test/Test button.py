#нажатие кнопки

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def test_button():
    found_button = driver.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
    found_button.click()
    text_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Записаться на прием')]")
    text = text_element.text
    assert text == "Записаться на прием"
    driver.quit()