from src import get_timed_loop_from_config, currencies_list_from_config, get_exchange_data, convert_dic_to_list
from module import CurrencyExchangeRepository
import threading

LOOP_TIME = get_timed_loop_from_config()


def fetch_and_upload_to_db():
    threading.Timer(LOOP_TIME, fetch_and_upload_to_db).start()
    currencies_list = currencies_list_from_config()
    exchange_data = get_exchange_data()

    exchange_data = {key: value for (key, value) in dict(exchange_data).items() if key in currencies_list}

    list_of_dic = convert_dic_to_list(exchange_data)

    CurrencyExchangeRepository.upload_to_db(list_of_dic)

    print("DB has been updated.")


if __name__ == "__main__":
    fetch_and_upload_to_db()
