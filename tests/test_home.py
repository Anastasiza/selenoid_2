from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

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

def test_logo(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        browser.get(base_url)
        assert WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'logo'))
        )
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста

def test_banner(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url)
        banner = browser.find_element(By.XPATH, '//*[@id="carousel-banner-0"]')
        assert banner
        time.sleep(2)
    finally:
        browser.quit()

def test_cart_button(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url)
        cart = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
        assert cart
        time.sleep(2)
    finally:
        browser.quit()

def test_featured(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url)
        featured = browser.find_element(By.XPATH, '//*[@id="content"]/h3')
        assert featured
        time.sleep(2)
    finally:
        browser.quit()

def test_carusel_banner(base_url):
    browser = setup_browser()
    try:
        browser.get(base_url)
        carusel = browser.find_element(By.XPATH, '//*[@id="carousel-banner-1"]')
        assert carusel
    finally:
        browser.quit()