from utils import convert_dic_to_list, currencies_list_from_config, get_exchange_data, kafka_set_up
from module import MongoClass

producer = kafka_set_up()
topicName = 'get_data_from_mongo'

currencies_list = currencies_list_from_config()

exchange_data = get_exchange_data()

exchange_data = {key: value for (key, value) in dict(exchange_data).items() if key in currencies_list}

list_of_dic = convert_dic_to_list(exchange_data)
MongoClass.upload_to_db(list_of_dic)

producer.send(topicName, "stocks update in db")
producer.flush()
