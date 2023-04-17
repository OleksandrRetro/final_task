from core.env import Env
from exceptions.env_not_found_exception import EnvNotFoundException
from utils.config_reader import ConfigReader


def get_base_ui_url(env: str) -> str:
    environment: str = env.lower()
    values: list = [member.value for member in Env]
    if environment in values:
        return ConfigReader(f"app_{environment}.ini").config_section_dict("SELENIUM").get("baseurl")
    else:
        raise EnvNotFoundException(env)


def get_base_api_url(env: str) -> str:
    environment: str = env.lower()
    values: list = [member.value for member in Env]
    if environment in values:
        return ConfigReader(f"app_{environment}.ini").config_section_dict("API").get("baseurl")
    else:
        raise EnvNotFoundException(env)
