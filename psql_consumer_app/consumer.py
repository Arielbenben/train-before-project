import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from mongo_consumer_app.repository.students_repository import insert_relationship
from psql_consumer_app.psql_repository import insert_student, insert_life_style, insert_performance, insert_review, \
    insert_teacher, insert_class


load_dotenv(verbose=True)


def consume():
    consumer = KafkaConsumer(
        os.environ['INSERT_PSQL'],
        bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
        value_deserializer= lambda value: json.loads(value.decode('utf-8')),
        auto_offset_reset='latest'
    )

    for message in consumer:
        match message.key.decode('utf-8'):
            case 'profile':
                insert_student(message.value)
            case 'life style':
                insert_life_style(message.value)
            case 'performance':
                insert_performance(message.value)
            case 'review':
                insert_review(message.value)
            case 'teacher':
                insert_teacher(message.value)
            case 'class':
                insert_class(message.value)
            case 'relation':
                insert_relationship(message.value)

        print(f"Recieved: {message.key}: {message.value}")