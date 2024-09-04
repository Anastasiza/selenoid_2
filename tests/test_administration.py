from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Функция для настройки браузера с использованием Selenoid
def setup_browser():
    options = Options()
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "latest",
        "selenoid:options": {
            "enableVNC": True,    # Включение VNC для визуализации тестов, если нужно
            "enableVideo": False  # Отключение записи видео, можно включить при необходимости
        }
    }

    # Подключение к Selenoid серверу
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # URL вашего Selenoid сервера
        options=options,
        desired_capabilities=capabilities
    )
    return browser

def test_header(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        browser.get(base_url + "/administration/")
        header = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="content"]/div/div/div/div/div[1]'))
        )
        assert header
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста

def test_username(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/administration/")
        username = browser.find_element(By.XPATH, '//*[@id="input-username"]')
        assert username
    finally:
        browser.quit()

def test_password(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/administration/")
        password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
        assert password
    finally:
        browser.quit()

def test_button(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/administration/")
        button = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[3]/button')
        assert button
    finally:
        browser.quit()

def test_lable_username(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/administration/")
        lable = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[1]/label')
        assert lable
    finally:
        browser.quit()

def test_lable_password(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/administration/")
        lable = browser.find_element(By.XPATH, '//*[@id="form-login"]/div[2]/label')
        assert lable
    finally:
        browser.quit()

