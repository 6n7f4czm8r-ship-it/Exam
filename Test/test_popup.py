# закрытие всплывающего окна
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://perm.medsi.ru/')
driver.maximize_window()
driver.implicitly_wait(10)

def test_button_2():
    try:
        close_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.youRegion__btn-t1.btn-yellow.confirmRegion"))
        )
        close_button.click()
        print("Всплывающее окно закрыто")
    except Exception as e:
        print("Окно не появилось")

    pass
