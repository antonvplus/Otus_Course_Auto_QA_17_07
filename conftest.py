import pytest
from selenium import webdriver
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Selecting browser (chrome, firefox)")
    parser.addoption("--base-url", action="store", default="http://localhost:8081/", help="Specify the base URL for opencart")

@pytest.fixture(scope="function")
def base_url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    if request.config.getoption('browser') == 'chrome':
        options = Options()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
    elif request.config.getoption('browser') == 'firefox':
        browser = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: '{request.config.getoption('browser')}'")
    yield browser
    browser.quit()
