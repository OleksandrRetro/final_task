import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def pages_init(self, pages):
        self.pages = pages
