from configparser import ConfigParser
from kafka import KafkaProducer
import json


def config_file_setup():
    config_file = "config.ini"
    config = ConfigParser()
    config.read(config_file)

    return config


def get_threshold_from_config():
    config = config_file_setup()
    threshold = int(config.get("threshold", "threshold_value"))

    return threshold


def get_timed_loop_from_config():
    config = config_file_setup()
    seconds = config.get("loop_time", "run_every")
    seconds = int(seconds)

    return seconds


def filter_by_threshold(dic):
    threshold = get_threshold_from_config()
    filtered_dic = [stock for stock in dic if not (stock['value'] <= threshold)]

    return filtered_dic


def get_mongo_url():
    config = config_file_setup()
    url = config.get("local_mongo_url", "url")

    return url


def kafka_set_up():
    config = config_file_setup()
    kafka_port = config.get("kafka_port", "port")
    kafka_topic = config.get("kafka_topic", "topic")

    bootstrap_servers = [kafka_port]
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    producer = KafkaProducer()
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    return {"kafka_producer": producer, "kafka_topic": kafka_topic}
