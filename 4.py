from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Небходимо выполнить:
#1. Зайти на главную страницу
#2. Заполнить поле Username
#3. Заполнить поле Password
#4. Нажать кнопку Login

# Константы
URL = 'https://www.saucedemo.com'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# Определение драйвера
def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
# открытие страницы
def open_page(driver, URL):
    driver.get(URL)
# поиск по ID
def get_element_by_id(driver, locator):
    element = driver.find_element(By.ID, locator)
    return element
# ввод данных
def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)
# нажатие на кнопку
def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()

#0 получение драйвера
driver = get_driver()
#1
open_page(driver, URL)
#2
element_send_keys(driver, 'user-name', LOGIN)
#3
element_send_keys(driver, 'password', PASSWORD)
#4
element_click(driver, 'login-button')