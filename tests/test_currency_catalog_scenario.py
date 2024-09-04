from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.catalog_page import CatalogPage

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

def test_currency_catalog(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        cp = CatalogPage(browser, base_url)
        cp.get_catalog_page()
        cp.change_currency()
        assert cp.get_actual_currency() == '£'
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста