from db import get_all_stocks
from configparser import ConfigParser

config_file = "../config.ini"
config = ConfigParser()
config.read(config_file)

threshold = int(config.get("threshold", "threshold_value"))

stocks = get_all_stocks()

print(stocks)
print(threshold)
