import csv
import json
import os
from producer_app.kafka_service.producer import produce


def read_csv(csv_path: str):
    try:
        with open(csv_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_json(json_path: str):
    try:
        with open(json_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        return str(e)


students_profile_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\students-profiles.csv'
students_life_style_path = "C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\student_lifestyle.csv"
students_course_performance_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\student_course_performance.csv'
reviews_students_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\reviews_with_students.csv'

academic_network_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\academic_network.json'


mongo_topic = os.environ['INSERT_MONGO']
psql_topic = os.environ['INSERT_PSQL']
elastic_topic = os.environ['INSERT_ELASTIC']
neo4j_topic = os.environ['INSERT_NEO$J']


def read_students_profile():
    students_profile = read_csv(students_profile_path)
    batch_size = 200
    batch = []

    for student in students_profile:
        batch.append(student)

        if len(batch) == batch_size:
            produce(mongo_topic, batch, 'profile')
            batch = []

    if batch:
        produce(mongo_topic, batch, 'profile')


def read_student_life_style():
    students_life_style = read_csv(students_life_style_path)
    batch_size = 200
    batch = []

    for life_style in students_life_style:
        batch.append(life_style)

        if len(batch) == batch_size:
            produce(mongo_topic, batch, 'life style')
            batch = []
    if batch:
        produce(mongo_topic, batch, 'life style')


def read_students_course_performance():
    students_course_performance = read_csv(students_course_performance_path)
    batch_size = 200
    batch = []

    for performance in students_course_performance:
        batch.append(performance)

        if len(batch) == batch_size:
            produce(mongo_topic, batch, 'performance')
            batch = []

    if batch:
        produce(mongo_topic, batch, 'performance')


def read_reviews_students():
    reviews_students = read_csv(reviews_students_path)
    batch_size = 200
    mongo_batch = []
    elastic_batch = []

    for review in reviews_students:
        mongo_batch.append(review)
        elastic_batch.append(review)

        if len(mongo_batch) == batch_size:
            produce(mongo_topic, mongo_batch, 'review')
            produce(elastic_topic, elastic_batch, 'review')
            mongo_batch = []
            elastic_batch = []

    if mongo_batch:
        produce(mongo_topic, mongo_batch, 'review')
        produce(elastic_topic, elastic_batch, 'review')


def send_batch_to_mongo(topic, batch, batch_type):
    if batch:
        produce(topic, batch, batch_type)


def process_teachers(teachers):
    teacher_batch = []
    batch_size = 200
    for teacher in teachers:
        teacher_batch.append(teacher)
        if len(teacher_batch) == batch_size:
            send_batch_to_mongo(mongo_topic, teacher_batch, 'teacher')
            teacher_batch = []

    send_batch_to_mongo(mongo_topic, teacher_batch, 'teacher')


def process_classes(classes):
    class_batch = []
    batch_size = 200
    for cla in classes:
        class_batch.append(cla)
        if len(class_batch) == batch_size:
            send_batch_to_mongo(mongo_topic, class_batch, 'class')
            class_batch = []

    send_batch_to_mongo(mongo_topic, class_batch, 'class')


def process_relationships(relationships):
    relation_batch = []
    batch_size = 200
    for relation in relationships:
        relation_batch.append(relation)
        if len(relation_batch) == batch_size:
            send_batch_to_mongo(mongo_topic, relation_batch, 'relation')
            send_batch_to_mongo(neo4j_topic, relation_batch, 'relation')
            relation_batch = []

    send_batch_to_mongo(mongo_topic, relation_batch, 'relation')
    send_batch_to_mongo(neo4j_topic, relation_batch, 'relation')


def read_academic_network():
    academic_network = read_json(academic_network_path)

    process_teachers(academic_network['teachers'])
    process_classes(academic_network['classes'])
    process_relationships(academic_network['relationships'])


def read_all_files():
    # read_students_profile()
    # read_student_life_style()
    # read_students_course_performance()
    # read_reviews_students()
    read_academic_network()

    return