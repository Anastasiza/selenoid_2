
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

def test_product_image(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        browser.get(base_url + "/en-gb/product/macbook")
        product = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/a/img'))
        )
        assert product
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста

def test_title(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/product/macbook")
        title = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/h1')
        assert title
    finally:
        browser.quit()

def test_prise(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/product/macbook")
        prise = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[2]/li[1]/h2/span')
        assert prise
    finally:
        browser.quit()

def test_input_qantiti(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/product/macbook")
        qantiti = browser.find_element(By.XPATH, '//*[@id="input-quantity"]')
        assert qantiti
    finally:
        browser.quit()

def test_button_card(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url + "/en-gb/product/macbook")
        button = browser.find_element(By.XPATH, '//*[@id="button-cart"]')
        assert button
    finally:
        browser.quit()