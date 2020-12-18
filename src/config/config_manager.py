"""load the configuration for the project"""


class ConfigManager:
    """This class provides a simple way to load configuration files"""

    def __init__(self, filename):
        if filename is None:
            raise Exception("No configuration file found!")
        self.filename = filename

    def parse(self) -> dict:
        """opens the configuration file and returns the configuration"""
        with open(self.filename) as file:
            lines = file.readlines()
        configuration = {}
        for line in lines:
            config = line.strip().split(":")
            configuration[config[0].strip()] = config[1].strip()
        return configuration

    def save(self, configuration, config_file=None) -> None:
        """save the configuration"""
        if configuration is None:
            raise Exception(
                "Expected a configuration, got {}".format(configuration))
        if config_file is None:
            config_file = self.filename
        with open(config_file, mode="a") as file:
            for x in configuration:
                file.write(f"{x}:{configuration[x]}")
