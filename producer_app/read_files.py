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


students_profile_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\student_lifestyle.csv'
students_life_style_path = "C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\student_lifestyle.csv"
students_course_performance_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\student_course_performance.csv'
reviews_students_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\reviews_with_students.csv'

academic_network_path = 'C:\\Users\\relbh\\Desktop\\training_project\\proj_data\\academic_network.json'



def read_students_profile():
    students_profile = read_csv(students_profile_path)
    student_topic = os.environ['INSERT_STUDENT']

    for student in students_profile:
        produce(student_topic, student)


def read_student_life_style():
    students_life_style = read_csv(reviews_students_path)
    life_style_topic = os.environ['INSERT_LIFE_STYLE']

    for life_style in students_life_style:
        produce(life_style_topic, life_style)


def read_students_course_performance():
    students_course_performance = read_csv(reviews_students_path)
    life_style_topic = os.environ['INSERT_PERFORMANCE']

    for performance in students_course_performance:
        produce(life_style_topic, performance)


def read_reviews_students():
    reviews_students = read_csv(reviews_students_path)
    review_topic = os.environ['INSERT_REVIEW']

    for review in reviews_students:
        produce(review_topic, review)


def read_academic_network():
    academic_network = read_json(academic_network_path)
    teacher_topic = os.environ.get('INSERT_TEACHER')
    class_topic = os.environ.get('INSERT_CLASS')
    relationship_topic = os.environ.get('INSERT_RELATIONSHIP')

    for teacher in academic_network['teachers']:
        produce(teacher_topic, teacher)
    for cla in academic_network['classes']:
        produce(class_topic, cla)
    for relation in academic_network['relationships']:
        produce(relationship_topic, relation)


def read_all_files():
    read_students_profile()
    read_student_life_style()
    read_students_course_performance()
    read_reviews_students()
    read_academic_network()
    
    return