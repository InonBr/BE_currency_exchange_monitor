from kafka import KafkaConsumer
from src import string_to_list, webhook_post_request, get_kafka_data

kafka_data = get_kafka_data()
consumer = KafkaConsumer(kafka_data["kafka_topic"], bootstrap_servers=[kafka_data["kafka_port"]])

if __name__ == "__main__":
    for data in consumer:
        decoded_data = data.value.decode('utf-8')
        decoded_data = string_to_list(decoded_data)

        response = webhook_post_request(decoded_data)

        print(f"response code: {response}")
