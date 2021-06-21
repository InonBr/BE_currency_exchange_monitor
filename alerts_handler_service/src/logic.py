import requests
import json
from configparser import ConfigParser


def config_file_setup():
    config_file = "config.ini"
    config = ConfigParser()
    config.read(config_file)

    return config


def get_kafka_data():
    config = config_file_setup()

    kafka_port = config.get("kafka_port", "port")
    kafka_topic = config.get("kafka_topic", "topic")

    return {"kafka_port": kafka_port, "kafka_topic": kafka_topic}


def string_to_list(currencies_list):
    currencies_list = list(eval(currencies_list))

    return currencies_list


def webhook_post_request(decoded_data):
    config = config_file_setup()

    currencies_list = config.get("webhook", "url")

    response = requests.post(
        currencies_list,
        data=json.dumps(decoded_data),
        headers={'Content-Type': 'application/json'})

    return response
