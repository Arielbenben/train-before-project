from pymongo import MongoClient


client = MongoClient('mongodb://172.19.191.59:27017')
students_data_db = client['students_data']

student_collection = students_data_db['students']
teacher_collection = students_data_db['teachers']
class_collection = student_collection['classes']
review_collection = student_collection['reviews']
relationship_collection = student_collection['relationships']
