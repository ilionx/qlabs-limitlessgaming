"""load the configuration for the project"""
import json


class ConfigManager:
    """
    This class provides a simple way to load configuration files

    Attributes
    ----------
    filename:str
        The relative path to the configuration file
    """

    def __init__(self, configuration=None, filename=None) -> None:
        if configuration is None:
            self.configuration = {}
        else:
            self.configuration = configuration
        if filename is not None:
            self.filename = filename
        else:
            self.filename = "Config.json"

    def load(self, filename=None) -> dict:
        if filename is None:
            filename = self.filename
        with open(filename, "r") as config_file:
            self.configuration = json.load(config_file)

    def save(self, filename=None, configuration=None) -> None:
        if filename is None:
            filename = self.filename
        if configuration is None:
            configuration = self.configuration

        with open(filename, "w") as config_file:
            json.dump(configuration, config_file)

    def __getitem__(self, item):
        return self.configuration[item]

    def __call__(self, *args, **kwds) -> dict:
        return self.configuration
