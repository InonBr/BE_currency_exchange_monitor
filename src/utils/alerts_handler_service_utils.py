import requests
import json
from configparser import ConfigParser


def string_to_list(currencies_list):
    currencies_list = list(eval(currencies_list))

    return currencies_list


def webhook_post_request(decoded_data):
    config_file = "config.ini"
    config = ConfigParser()
    config.read(config_file)

    currencies_list = config.get("webhook", "url")

    response = requests.post(
        currencies_list,
        data=json.dumps(decoded_data),
        headers={'Content-Type': 'application/json'})

    return response
