from module import MongoClass
from utils import get_threshold_from_config, filter_by_threshold, kafka_set_up
from kafka import KafkaConsumer

producer = kafka_set_up()
topicName = 'alert_created'
consumer = KafkaConsumer('get_data_from_mongo', bootstrap_servers=['localhost:9092'])

threshold = get_threshold_from_config()

stocks = MongoClass.get_all_stocks()

stocks = filter_by_threshold(stocks, threshold)

for i in consumer:
    if len(stocks) > 0:
        producer.send(topicName, stocks)
        producer.flush()
