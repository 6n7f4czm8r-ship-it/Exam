import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@allure.id("4")
@allure.label("Пустое поле")
@allure.title("Вход без данных пользователя")
@allure.description("Тест, проверяющий регистрацию без ввода данных")
@allure.severity("Normal")

def test_none_input(driver_init):
    with allure.step("Переход на сайт 'Медси'"):
        driver_init.get('https://perm.medsi.ru/')

    with allure.step("Скролим страницу вниз"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем кнопку 'Записаться на прием'"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
        found_button.click()

    with allure.step("Переход для работы в новом окне"):
        windows = driver_init.window_handles
        driver_init.switch_to.window(windows[1])

    with allure.step("Скролим страницу вниз"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем на поле для ввода данных"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "input.smed-input__native")
        found_button.click()

    with allure.step("Нажимаем кнопку 'Продолжить'"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "span.smed-base-button__content")
        found_button.click()

    with allure.step("Проверяем, что на экране появился текст 'Некорректный номер мобильного телефона'"):
        text_element = driver_init.find_element(By.CSS_SELECTOR, "p.smed-text_body-sm")
        text = text_element.text
        assert not text == "Некорректный номер мобильного телефона"
        # driver.quit()