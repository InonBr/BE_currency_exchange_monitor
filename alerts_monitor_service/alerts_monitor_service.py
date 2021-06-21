from module import CurrencyExchangeRepository
from src import filter_by_threshold, get_timed_loop_from_config, kafka_set_up
import threading

LOOP_TIME = get_timed_loop_from_config()


def collect_data_from_db_and_alert():
    threading.Timer(LOOP_TIME, collect_data_from_db_and_alert).start()

    kafka_dic = kafka_set_up()

    stocks = CurrencyExchangeRepository.get_all_stocks()
    stocks = filter_by_threshold(stocks)

    if stocks:
        kafka_dic["kafka_producer"].send(kafka_dic["kafka_topic"], stocks)
        kafka_dic["kafka_producer"].flush()
        print(kafka_dic["kafka_topic"])


if __name__ == "__main__":
    collect_data_from_db_and_alert()
