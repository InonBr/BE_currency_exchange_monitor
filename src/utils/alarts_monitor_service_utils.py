from configparser import ConfigParser


def filter_by_threshold(dic, threshold):
    filtered_dic = [stock for stock in dic if not (stock['value'] <= threshold)]

    return filtered_dic


def get_threshold_from_config():
    config_file = "../config.ini"
    config = ConfigParser()
    config.read(config_file)
    threshold = int(config.get("threshold", "threshold_value"))

    return threshold
