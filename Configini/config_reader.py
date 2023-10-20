import configparser

class ConfigReader:
    def __init__(self, config_file_path):
        self.config = configparser.ConfigParser()
        self.config.read(config_file_path)

    def get_app_config(self):
        return self.config["app"]

    def get_database_config(self):
        return self.config["database"]
