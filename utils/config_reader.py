import configparser
import os

from constants.global_const import RESOURCES_PATH


class ConfigReader:

    def __init__(self, ini_file: str) -> None:
        self.config: configparser = configparser.ConfigParser()
        self.file_path: str = os.path.join(RESOURCES_PATH, ini_file)
        self.config.read(self.file_path)

    def config_section_dict(self, section):
        section_dict = {}
        section_keys = self.config.options(section)
        for key in section_keys:
            try:
                section_dict[key] = self.config.get(section, key)
            except configparser.NoSectionError:
                print(f"There are no section [{key}].")
                section_dict[key] = None
        return section_dict
