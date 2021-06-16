from configparser import ConfigParser
import requests


def get_exchange_data():
    exchange_api = 'https://api.exchangerate.host/latest'
    response = requests.get(exchange_api)
    exchange_data = response.json()["rates"]

    return exchange_data


def currencies_list_from_config():
    config_file = "../config.ini"
    config = ConfigParser()
    config.read(config_file)

    currencies_list = config.get("currencies", "currencies")
    currencies_list = list(currencies_list.split(", "))

    return currencies_list


def convert_dic_to_list(dic):
    list_of_dic = [{key: value} for key, value in dic.items()]
    list_of_dic = create_mongo_dic(list_of_dic)

    return list_of_dic


def create_mongo_dic(list_of_dic):
    for dic in list_of_dic:
        dic["name"] = list(dic.keys())[0]
        dic["value"] = dic[dic["name"]]
        del dic[dic["name"]]

    return list_of_dic
