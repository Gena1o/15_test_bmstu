from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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


#функции
# Определение драйвера
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.implicitly_wait(10)
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

#авторизация по логину и паролю
def login(driver, login, password):
    element_send_keys(driver, 'user-name', login)
    element_send_keys(driver, 'password',  password)
    element_click(driver, 'login-button')



# рабочий код
driver = get_driver()
open_page(driver, URL)
login(driver=driver, login=LOGIN, password=PASSWORD)

driver.quit()