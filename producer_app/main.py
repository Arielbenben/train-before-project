from producer_app.kafka_service.init_topics import init_topics
from producer_app.read_files import read_all_files



if __name__ == '__main__':
    init_topics()
    read_all_files()