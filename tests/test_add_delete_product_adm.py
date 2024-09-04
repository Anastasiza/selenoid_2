from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_objects.admin_login_page import AdminLoginPage
from page_objects.admin_page import AdminPage

admin_page = None


# Настройка браузера для работы с Selenoid
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
        command_executor='http://localhost:4444/wd/hub',  # URL вашего Selenoid
        options=options,
        desired_capabilities=capabilities
    )
    return browser


def test_add_product(base_url):
    global admin_page
    browser = setup_browser()  # Создаем экземпляр браузера через Selenoid

    try:
        product_name = "AApple"

        adm_login = AdminLoginPage(browser, base_url)
        adm_login.get_admin_page()
        token = adm_login.login()

        admin_page = AdminPage(browser, base_url, token)
        admin_page.get_admin_page()
        actual_saves_product_name = admin_page.add_product_page(product_name)
        assert actual_saves_product_name == product_name + "\nEnabled"
    finally:
        browser.quit()  # Закрываем браузер после выполнения теста


def test_delete_product(base_url):
    global admin_page

    if admin_page is None:
        raise ValueError("Admin page is not initialized. Please run test_add_product first.")

    browser = admin_page.browser  # Используем тот же браузер, что и в test_add_product

    try:
        no_result = admin_page.delete_product()
        assert no_result == "No results!"
    finally:
        browser.quit()  # Закрываем браузер после выполнения теста