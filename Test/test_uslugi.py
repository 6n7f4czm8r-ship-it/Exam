# #выбор услуги и добавление в корзину
# import allure
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
#
# driver.get('https://perm.medsi.ru/')
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# def test_button(driver_init):
#     with allure.step("Открытие сайта Медси"):
#         driver_init.get("https://perm.medsi.ru/")
#
#     with allure.step("Скролим страницу вниз"):
#         driver_init.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     with allure.step("Нажимаем на кнопку 'Анализы'"):
#         found_button = driver_init.find_element(By.ID, "navP2")
#         found_button.click()

    # with allure.step("Переход для работы в новом окне"):
    #     windows = driver_init.window_handles
    #     driver_init.switch_to.window(windows[1])

    # with allure.step("Проверяем что на экране есть текст 'Записаться на приём'"):
    #     text_element = driver_init.find_element(By.XPATH, "//h1[contains(text(), 'Записаться на прием')]")
    #     text = text_element.text
    #     assert text == "Записаться на прием"