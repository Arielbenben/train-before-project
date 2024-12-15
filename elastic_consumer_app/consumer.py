import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from elastic_consumer_app.elastic_repository import insert_review_to_elastic


load_dotenv(verbose=True)


def consume():
    consumer = KafkaConsumer(
        os.environ['INSERT_REVIEW'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer= lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        insert_review_to_elastic(message.value)
        print(f"Recieved: {message.key}: {message.value}")