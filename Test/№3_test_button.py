import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@allure.id("2")
@allure.label("Переход на другую страницу")
@allure.title("Переход по вкладке на другую страницу")
@allure.description("Тест, проверяющий нажатие кнопки и переход на другую страницу")
@allure.severity("Critical")

def test_button(driver_init):
    with allure.step("Открытие сайта Медси"):
        driver_init.get("https://perm.medsi.ru/")

    with allure.step("Скролим страницу вниз"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем на кнопку 'Записаться на прием'"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
        found_button.click()

    with allure.step("Проверяем что на экране есть текст 'Войти в личный кабинет'"):
        text_element = driver_init.find_element(By.CSS_SELECTOR, "h1._header_tpzfr_11")
        text = text_element.text
        assert text == "Войти в личный кабинет"