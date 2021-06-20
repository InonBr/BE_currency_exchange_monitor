from utils import convert_dic_to_list, currencies_list_from_config, get_exchange_data
from module import MongoClass
import threading


def fetch_and_upload_to_db():
    # CR: hardcoded value should be in the config
    # will run it every 10 seconds
    threading.Timer(10.0, fetch_and_upload_to_db).start()

    currencies_list = currencies_list_from_config()

    exchange_data = get_exchange_data()

    exchange_data = {key: value for (key, value) in dict(exchange_data).items() if key in currencies_list}

    list_of_dic = convert_dic_to_list(exchange_data)
    MongoClass.upload_to_db(list_of_dic)

    print("DB has been updated.")


fetch_and_upload_to_db()
