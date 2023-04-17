from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LandingPage(BasePage):
    __HEADER_SELECTOR: str = (By.CSS_SELECTOR, "h1.heading")
    __ABTESTING_LINK_SELECTOR: str = (By.CSS_SELECTOR, "a[href='/abtest']")

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self.wait_until_page_loaded()

    def get_header_text(self) -> str:
        return self.get_text(self.__HEADER_SELECTOR)

    def click_a_b_testing_link(self) -> None:
        self.click(self.__ABTESTING_LINK_SELECTOR)
