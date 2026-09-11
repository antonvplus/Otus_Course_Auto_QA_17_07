import pytest
from selenium import webdriver
from typing import Generator
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsForFirefox
import datetime
from pathlib import Path
import os
import allure
from logger_config import logger
import logging


logger = logging.getLogger("Logger.Fixture")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Selecting browser (chrome, firefox)")
    parser.addoption("--OS", action="store", default="windows", help="Selecting OS (windows, linux). If Linux is selected, "
                                                                     "the browser will be launched in non-graphical interface mode.")
    parser.addoption("--base-url", action="store", default="http://localhost:8081/", help="Specify the base URL for PrestaShop")
    parser.addoption("--executor", action="store", default="local", help="local or selenoid")

@pytest.fixture(scope="function")
def base_url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--base-url")

@pytest.fixture(scope="function")
def browser(request: pytest.FixtureRequest) -> Generator[WebDriver, None, None]:
    if request.config.getoption('--executor') == 'selenoid' or request.config.getoption('--executor') == 'ggr':
        logger.debug("Выбран браузер Chrome")
        selenoid_options = {
            "enableVNC": True,
            "enableVideo": False
        }
        options = Options()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "120.0")
        options.set_capability("selenoid:options", selenoid_options)
        if request.config.getoption('--executor') == "ggr":
            logger.debug("Запуск через ggr , selenoid")
            browser = webdriver.Remote(command_executor="http://ggr:4444/wd/hub", options=options)
        else:
            logger.debug("Запуск через selenoid")
            browser = webdriver.Remote(command_executor="http://selenoid:4444/wd/hub", options=options)
    else:
        if request.config.getoption('--browser') == 'chrome':
            logger.debug("Выбран браузер Chrome")
            logger.info(f"Старт теста: {request.node.name}")
            with allure.step("Используем браузер Chrome"):
                options = Options()
                if request.config.getoption('--OS') == 'windows':
                    options.add_argument("--start-maximized")
                elif request.config.getoption('OS') == 'linux':
                    options.add_argument("--window-size=1920,1080")
                    options.add_argument("--headless=new")
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")
                    logger.debug("Запуска браузера без графического интерфейса")
            browser = webdriver.Chrome(options=options)
        elif request.config.getoption('--browser') == 'firefox':
            logger.debug("Выбран браузер Firefox")
            logger.info(f"Старт теста: {request.node.name}")
            options = OptionsForFirefox()
            if request.config.getoption('--OS') == 'linux':
                options.add_argument("--headless")
                logger.debug("Запуска браузера без графического интерфейса")
            with allure.step("Используем браузер Firefox"):
                browser = webdriver.Firefox(options=options)
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

