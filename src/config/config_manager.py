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
        """
        This class provides a simple way to load configuration files

        Parameters
        ----------
        configuration: dict
        filename: str
        """
        if configuration is None:
            self.configuration = {}
        else:
            self.configuration = configuration
        if filename is not None:
            self.filename = filename
        else:
            self.filename = "src/config.json"
        self.load()

    def load(self) -> None:
        with open(self.filename, "r") as config_file:
            self.configuration.update(json.load(config_file))

    def save(self) -> None:
        with open(self.filename, "w") as config_file:
            json.dump(self.configuration, config_file)

    def __getitem__(self, item) -> dict:
        if item not in self.configuration:
            return False
        return self.configuration[item]

    def __call__(self, *args, **kwds) -> dict:
        return self.configuration


if __name__ == "__main__":
    cfm = ConfigManager(filename="examples/sample.json")
    print(cfm())
    cfm = ConfigManager(filename="examples/Config.json", configuration={1: 2})
    print(cfm())
