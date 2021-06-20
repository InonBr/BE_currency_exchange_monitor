from module import MongoClass
from utils import get_threshold_from_config, filter_by_threshold, kafka_set_up
import threading

# CR: do not just call the code directly but use a bootstrapping function "__main__"

def collect_data_from_db_and_alert():
    # CR: hardcoded value should be in the config
    # will run it every 13 seconds
    threading.Timer(13.0, collect_data_from_db_and_alert).start()

    producer = kafka_set_up()
    # CR: hardcoded value use CONST or config
    topic_name = 'alert_created'

    threshold = get_threshold_from_config()

    stocks = MongoClass.get_all_stocks()

    stocks = filter_by_threshold(stocks, threshold)

    if stocks:
        producer.send(topic_name, stocks)
        producer.flush()
        print(topic_name)


collect_data_from_db_and_alert()
