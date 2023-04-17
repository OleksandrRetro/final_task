import requests
from requests import Response


class ControllerApi:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_user_by_id(self, id) -> dict:
        return requests.get(f"{self.url}/users/{id}").json()

    def post_user(self, body) -> Response:
        return requests.post(f"{self.url}/users", json=body)
