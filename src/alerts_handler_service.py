from kafka import KafkaConsumer
from utils import string_to_list

consumer = KafkaConsumer('alert_created', bootstrap_servers=['localhost:9092'])

for data in consumer:
    decoded_data = data.value.decode('utf-8')
    decoded_data = string_to_list(decoded_data)

    print(type(decoded_data))
    print(decoded_data)
