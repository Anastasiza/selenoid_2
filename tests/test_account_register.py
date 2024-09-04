from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# Конфигурация для подключения к Selenoid
def setup_browser():
    # Настраиваем ChromeOptions
    options = Options()
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Настройка подключения к Selenoid
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
        command_executor='http://localhost:4444/wd/hub',  # URL Selenoid
        options=options,
        desired_capabilities=capabilities
    )
    return browser

def test_first_name():
    browser = setup_browser()
    browser.get("http://your-base-url.com/en-gb?route=account/register")
    first_name = WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="input-firstname"]')))
    assert first_name
    browser.quit()

def test_last_name():
    browser = setup_browser()
    browser.get("http://your-base-url.com/en-gb?route=account/register")
    last_name = browser.find_element(By.XPATH, '//*[@id="input-lastname"]')
    assert last_name
    browser.quit()

def test_mail():
    browser = setup_browser()
    browser.get("http://your-base-url.com/en-gb?route=account/register")
    mail = browser.find_element(By.XPATH, '//*[@id="input-email"]')
    assert mail
    browser.quit()

def test_password():
    browser = setup_browser()
    browser.get("http://your-base-url.com/en-gb?route=account/register")
    password = browser.find_element(By.XPATH, '//*[@id="input-password"]')
    assert password
    browser.quit()

def test_continue_input():
    browser = setup_browser()
    browser.get("http://your-base-url.com/en-gb?route=account/register")
    cont = browser.find_element(By.XPATH, '//*[@id="form-register"]/div/button')
    assert cont
    browser.quit()