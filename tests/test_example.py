from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

def test_check_title(base_url):
    browser = setup_browser()  # Настройка браузера через Selenoid
    try:
        browser.get(base_url)
        assert "Your Store" in browser.title
        time.sleep(3)
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста