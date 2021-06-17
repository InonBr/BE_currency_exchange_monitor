from module import MongoClass
from utils import get_threshold_from_config, filter_by_threshold, kafka_set_up
import threading


def collect_data_from_db_and_alert():
    # will run it every 35 seconds
    threading.Timer(35.0, collect_data_from_db_and_alert).start()

    producer = kafka_set_up()
    topic_name = 'alert_created'

    threshold = get_threshold_from_config()

    stocks = MongoClass.get_all_stocks()

    stocks = filter_by_threshold(stocks, threshold)

    if len(stocks) > 0:
        producer.send(topic_name, stocks)
        producer.flush()
        print("alert created")


collect_data_from_db_and_alert()
