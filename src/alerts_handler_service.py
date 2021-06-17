from kafka import KafkaConsumer
from utils import string_to_list, webhook_post_request

consumer = KafkaConsumer('alert_created', bootstrap_servers=['localhost:9092'])

for data in consumer:
    decoded_data = data.value.decode('utf-8')
    decoded_data = string_to_list(decoded_data)

    response = webhook_post_request(decoded_data)

    print(f"response code: {response}")
