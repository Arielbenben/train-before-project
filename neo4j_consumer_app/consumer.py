import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from neo4j_consumer_app.repository.relationship_repository import add_relationships

load_dotenv(verbose=True)


def consume():
    consumer = KafkaConsumer(
        os.environ['INSERT_NEO$J'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer= lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        add_relationships(message.value)
        print(f"Recieved: {message.key}: {message.value}")