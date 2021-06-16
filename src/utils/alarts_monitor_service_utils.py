from configparser import ConfigParser


def get_threshold_from_config():
    config_file = "../config.ini"
    config = ConfigParser()
    config.read(config_file)
    threshold = int(config.get("threshold", "threshold_value"))

    return threshold
