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

@allure.id("5")
@allure.label("Анализы")
@allure.title("Выбор анализов")
@allure.description("Тест, проверяющий выбор необходимого анализы и добавление его в корзину")
@allure.severity("Normal")

def test_lab(driver_init):
    with allure.step("Открытие сайта Медси"):
        driver_init.get("https://perm.medsi.ru/")

    with allure.step("Скролим страницу вниз"):
        driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    with allure.step("Нажимаем на кнопку 'Анализы'"):
        button = driver.find_element(By.ID, "navP2")
        button.click()

    # with allure.step("Нажимаем на поле для ввода данных"):
    #     found_button = driver_init.find_element(By.CLASS_NAME, "lb-test__price")
    #     found_button.click()

    # with allure.step("Ввод в поле поиска названия анализа"):
    #     found_button.send_keys('Общий анализ крови')
        # text_element = driver_init.find_element(By.XPATH, "//h1[contains(text(), 'Записаться на прием')]")
        # text = text_element.text
        # assert text == "Записаться на прием"