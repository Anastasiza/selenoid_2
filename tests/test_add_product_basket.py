from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.home_page import HomePage
from page_objects.basket_page import BasketPage


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
            "enableVNC": True,
            "enableVideo": False
        }
    }

    # Подключение к Selenoid
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',  # URL вашего Selenoid сервера
        options=options,
        desired_capabilities=capabilities
    )
    return browser


def test_add_product_basket(base_url):
    browser = setup_browser()  # Настройка браузера с использованием Selenoid

    try:
        hp = HomePage(browser, base_url)
        hp.get_home_page()
        hp.add_product_to_basket()

        pb = BasketPage(browser, base_url)
        pb.get_basket_page()

        assert pb.get_product_line()  # Проверка наличия товара в корзине
    finally:
        browser.quit()  # Закрываем браузер после выполнения теста