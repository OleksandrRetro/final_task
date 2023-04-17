from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver) -> None:
        self._driver: webdriver = driver
        self._wait: WebDriverWait = WebDriverWait(self._driver, 10)

    def get_text(self, web_element_locator: str) -> str:
        return self._wait.until(expected_conditions.visibility_of_element_located(web_element_locator)).text

    def click(self, web_element_locator: str) -> None:
        self._wait.until(expected_conditions.element_to_be_clickable(web_element_locator)).click()

    def wait_until_page_loaded(self) -> None:
        old_page: str = self._driver.find_element_by_tag_name('html')
        yield
        self._wait.until(expected_conditions.staleness_of(old_page))
