from module import MongoClass
from utils import get_threshold_from_config
from kafka import KafkaConsumer

consumer = KafkaConsumer('get_data_from_mongo', bootstrap_servers=['localhost:9092'])

threshold = get_threshold_from_config()

stocks = MongoClass.get_all_stocks()

for i in consumer:
    print(stocks)
    print(threshold)
