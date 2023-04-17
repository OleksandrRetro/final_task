import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from core.config import get_base_ui_url, get_base_api_url
from core.controller_api import ControllerApi
from core.env import Env
from pages.abtesting_page import ABTestingPage
from pages.landing_page import LandingPage


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     default="test",
                     help="environment to run on.",
                     choices=(Env.TEST, Env.DEV),
                     )


@pytest.fixture
def pages():
    landing_page = LandingPage(driver)
    abtesting_page = ABTestingPage(driver)
    return locals()


@pytest.fixture(autouse=True)
def create_driver(request):
    global driver
    opts = Options()
    opts.add_argument("--headless")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(get_base_ui_url(request.config.option.env))
    yield
    driver.quit()


@pytest.fixture
def controller(request):
    controller = ControllerApi(get_base_api_url(request.config.option.env))
    return locals()
