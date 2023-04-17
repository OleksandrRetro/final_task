import pytest


class BaseTest:
    @pytest.fixture(autouse=True)
    def controllers_init(self, controller):
        self.controller = controller
