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
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@allure.id("4")
@allure.label("Услуги")
@allure.title("Переход на страницу выбора услуг")
@allure.description("Тест, проверяющий переход на страницу с выбором услуг")
@allure.severity("Normal")

def test_crossing_page(driver_init):
    with allure.step("Нажимаем на кнопку 'Услуги'"):
        button = driver.find_element(By.ID, "navP")
        button.click()

    with allure.step("Проверяем, что на экране есть надпись 'Услуги в г. Пермь'"):
        text_element = driver.find_element(By.XPATH, "//h1[contains(text(), 'Услуги в г. Пермь')]")
        text = text_element.text
        assert text == "Услуги в г. Пермь"