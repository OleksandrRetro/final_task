from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage


class ABTestingPage(BasePage):
    __HEADER_SELECTOR: str = (By.CSS_SELECTOR, ".example h3")

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.wait_until_page_loaded()

    def get_header_text(self) -> str:
        return self.get_text(self.__HEADER_SELECTOR)
