from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="chrome"
    )
    parser.addoption(
        "--base_url", default="http://localhost"
    )


driver = None


@pytest.fixture()
def browser(request):
    global driver
    browser_name = request.config.getoption("--browser")
    if driver is None:
        if browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "firefox":
            driver = webdriver.Firefox()
    yield driver
    #driver.close()

@pytest.fixture()
def base_url(request):
    return request.config.getoption("--base_url")

