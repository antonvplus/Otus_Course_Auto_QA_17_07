import pytest
from selenium import webdriver
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
import datetime
from pathlib import Path
import os
import allure
from logger_config import logger
import logging

logger = logging.getLogger("Logger.Fixture")

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Selecting browser (chrome, firefox)")
    parser.addoption("--base-url", action="store", default="http://localhost:8081/", help="Specify the base URL for opencart")

@pytest.fixture(scope="function")
def base_url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    if request.config.getoption('browser') == 'chrome':
        logger.debug("Выбран браузер Chrome")
        logger.info(f"Старт теста: {request.node.name}")
        with allure.step("Используем браузер Chrome"):
            options = Options()
            options.add_argument("--start-maximized")
            browser = webdriver.Chrome(options=options)
    elif request.config.getoption('browser') == 'firefox':
        logger.debug("Выбран браузер Firefox")
        logger.info(f"Старт теста: {request.node.name}")
        with allure.step("Используем браузер Firefox"):
            browser = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: '{request.config.getoption('browser')}'")
    yield browser
    with allure.step("Закрываем браузер"):
        browser.quit()
        logger.debug("Браузер закрыт")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        browser = item.funcargs.get("browser")
        if browser:
            logger.error(f"Test failed: {item.nodeid}\n{report.longreprtext}")
            path = f"Screenshot_{datetime.datetime.now().strftime("%Y-%m-%d")}"
            if not Path(path).is_dir():
                Path(path).mkdir()
            file_name = f"screenshot_{item.name}_{datetime.datetime.now().strftime("%H-%M-%S")}.png"
            file_path = os.path.join(path, file_name)
            browser.save_screenshot(file_path)
            logger.info(f"Скриншот сохранен в {file_path}")
            allure.attach(browser.get_screenshot_as_png(), name=file_path, attachment_type=allure.attachment_type.PNG)

