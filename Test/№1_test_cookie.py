import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)

@allure.id("1")
@allure.label("Куки")
@allure.title("Закрытие всплывающего окна Cookie")
@allure.description("Тест, проверяющий принятие всплывающего окна Cookie-файлов")
@allure.severity("Normal")

def test_button_1(driver_init):
  try:
      close_button = WebDriverWait(driver, 30).until(
           EC.element_to_be_clickable((By.CSS_SELECTOR, "div.cookie-alert__button.js-save-cookie-btn"))
       )
      close_button.click()
      print("Всплывающее окно закрыто")
  except Exception as e:
      print("Окно не появилось")
      pass