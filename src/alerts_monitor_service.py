from module import MongoClass
from configparser import ConfigParser

config_file = "../config.ini"
config = ConfigParser()
config.read(config_file)

threshold = int(config.get("threshold", "threshold_value"))

stocks = MongoClass.get_all_stocks()

print(stocks)
print(threshold)
