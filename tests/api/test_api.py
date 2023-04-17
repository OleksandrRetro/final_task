import pytest

from constants.global_const import CONTROLLER
from models.user_model import UserModel
from tests.api.test_base import BaseTest


class TestSign(BaseTest):

    @pytest.mark.api
    def test_get_user_by_id(self):
        response = self.controller[CONTROLLER].get_user_by_id(2)
        assert response['data']['id'] == 2

    @pytest.mark.api
    @pytest.mark.parametrize("name, job",
                             [('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'),
                              ('John', 'Rambo'), ]
                             )
    def test_create_user(self, name, job):
        body = UserModel().create_custom_user(name, job)
        response = self.controller[CONTROLLER].post_user(body)
        assert response.status_code == 201
        assert response.json()['name'] == name
        assert response.json()['job'] == job
