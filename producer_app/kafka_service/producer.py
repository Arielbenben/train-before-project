from kafka import KafkaProducer
import os
import json


def produce(topic_name: str, message: str):
    producer = KafkaProducer(
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_serializer= lambda value: json.dumps(value).encode('utf-8')
    )
    producer.send(
        topic_name,
        value=message
    )