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

@allure.id("3")
@allure.label("Ввод данных в поле")
@allure.title("Ввод цифр в поле")
@allure.description("Тест, проверяющий ввод цифр в поле регистрации пользователя")
@allure.severity("Normal")

def test_data_input(driver_init):
    with allure.step("Открытие сайта 'Медси'"):
        driver_init.get('https://perm.medsi.ru/')

    with allure.step("Скроллим страницу в 'подвал' сайта"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем кнопку 'Записаться на прием'"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "a.btn.btn-yellow.for-utm-link")
        found_button.click()

    with allure.step("Переключаемся на работу в новом окне"):
        windows = driver_init.window_handles
        driver_init.switch_to.window(windows[1])

    with allure.step("Скролим страницу вниз"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем на поле ввода номера телефона"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "input.smed-input__native")
        found_button.click()

    with allure.step("Вводим рандомные цифры"):
        found_button.send_keys('0123456789')

    with allure.step("Нажимаем кнопку 'Продолжить'"):
        found_button = driver_init.find_element(By.CSS_SELECTOR, "span.smed-base-button__content")
        found_button.click()

    with allure.step("Проверяем, что на экране появился текст 'Отправили код в СМС'"):
        text_element = driver_init.find_element(By.CSS_SELECTOR, "p.smed-text_body-sm")
        text = text_element.text
        assert not text == "Отправили код в СМС."




