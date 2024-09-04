from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.admin_login_page import AdminLoginPage


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
            "enableVNC": True,  # Включение VNC для визуализации тестов (при необходимости)
            "enableVideo": False  # Отключение записи видео
        }
    }

    # Подключение к Selenoid
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # URL Selenoid сервера
        options=options,
        desired_capabilities=capabilities
    )
    return browser


def test_auth(base_url):
    browser = setup_browser()  # Инициализация браузера через Selenoid

    try:
        adm = AdminLoginPage(browser, base_url)
        adm.get_admin_page()
        adm.login()
        assert adm.lable()  # Проверка наличия элемента после входа
    finally:
        browser.quit()  # Закрытие браузера после выполнения теста

