from dotenv import load_dotenv
import os
from kafka import KafkaAdminClient
from kafka.admin import NewTopic


load_dotenv(verbose=True)


env_vars = ['INSERT_ELASTIC', 'INSERT_MONGO', 'INSERT_PSQL', 'INSERT_NEO$J']


def init_topics():
    admin_client = KafkaAdminClient(bootstrap_servers=os.environ['BOOTSTRAP_SERVERS'])

    topics = [os.environ.get(var) for var in env_vars if var in os.environ]
    topic_list = [
        NewTopic(
            name=topic,
            num_partitions=int(os.environ["NUM_PARTITIONS"]),
            replication_factor=int(os.environ["NUM_REPLICATION"])
        ) for topic in topics
    ]

    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topics created successfully!")
    except Exception as e:
        print(f"Error creating topics: {e}")
    finally:
        admin_client.close()