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

def test_search(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        browser.get(base_url + "/en-gb/catalog/")
        search = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="search"]/input'))
        )
        assert search
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста

def test_column(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/catalog/")
        column = browser.find_element(By.XPATH, '//*[@id="column-left"]')
        assert column
    finally:
        browser.quit()

def test_continue(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/catalog/")
        continue_button = browser.find_element(By.XPATH, '//*[@id="content"]/div/a')
        assert continue_button
    finally:
        browser.quit()

def test_breadcrumb(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/catalog/")
        breadcrumb = browser.find_element(By.XPATH, '//*[@id="error-not-found"]/ul')
        assert breadcrumb
    finally:
        browser.quit()

def test_container(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/catalog/")
        container = browser.find_element(By.XPATH, '/html/body/footer/div')
        assert container
    finally:
        browser.quit()