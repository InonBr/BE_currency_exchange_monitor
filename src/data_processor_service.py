from configparser import ConfigParser
import requests

config_file = "../config.ini"
config = ConfigParser()
config.read(config_file)

currencies_list = config.get("currencies", "currencies")
currencies_list = list(currencies_list.split(", "))

exchange_api = 'https://api.exchangerate.host/latest'
response = requests.get(exchange_api)

exchange_data = response.json()["rates"]

exchange_data = {key: value for (key, value) in dict(exchange_data).items() if key in currencies_list}

print(currencies_list)
print(exchange_data)