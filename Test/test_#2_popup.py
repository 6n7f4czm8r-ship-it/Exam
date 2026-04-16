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

@allure.id("2")
@allure.label("Всплывающее окно")
@allure.title("Закрытие всплывающего окна выбора региона")
@allure.description("Тест, проверяющий принятие всплывающего окна о выборе региона")
@allure.severity("Normal")

def test_button_2(driver_init):
    try:
        close_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.youRegion__btn-t1.btn-yellow.confirmRegion"))
        )
        close_button.click()
        print("Всплывающее окно закрыто")
    except Exception as e:
        print("Окно не появилось")
    pass
