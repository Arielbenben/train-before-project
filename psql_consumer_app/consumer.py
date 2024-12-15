import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer


load_dotenv(verbose=True)


# def consume():
#     consumer = KafkaConsumer(
#         os.environ['INSERT_PSQL'],
#         bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'],
#         value_deserializer= lambda value: json.loads(value.decode('utf-8')),
#         auto_offset_reset='latest'
#     )
#
#     for message in consumer:
#         if message.key in ['']
#         print(f"Recieved: {message.key}: {message.value}")