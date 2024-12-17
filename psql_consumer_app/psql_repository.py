from datetime import datetime
from psql_consumer_app.db.database import session_maker
from psql_consumer_app.db.models.class_ import Class
from psql_consumer_app.db.models.life_style import LifeStyle
from psql_consumer_app.db.models.performance import Performance
from psql_consumer_app.db.models.relationship import Relationship
from psql_consumer_app.db.models.reviews_students import ReviewsStudents
from psql_consumer_app.db.models.student import Student
from psql_consumer_app.db.models.teacher import Teacher



def insert_student(students: list):
    students_models = [Student(**student) for student in students]
    with session_maker() as session:
        session.add_all(students_models)
        session.commit()


def insert_life_style(life_styles: list):
    life_style_model = [LifeStyle(**ls) for ls in life_styles]
    with session_maker() as session:
        session.add_all(life_style_model)
        session.commit()


def insert_performance(performances: list):
    performance_model = [Performance(**p) for p in performances]
    with session_maker() as session:
        session.add_all(performance_model)
        session.commit()


def insert_review(reviews: list):
    review_model = []
    for review in reviews:
        review['date_time'] = datetime.strptime(review['date_time'], "%d-%m-%Y %H:%M")
        review_model.append(ReviewsStudents(**review))
    with session_maker() as session:
        session.add_all(review_model)
        session.commit()


def insert_teacher(teachers: list):
    teacher_model = [Teacher(**teacher) for teacher in teachers]
    with session_maker() as session:
        session.add_all(teacher_model)
        session.commit()


def insert_class(classes: list):
    class_model = [Class(**cl) for cl in classes]
    with session_maker() as session:
        session.add_all(class_model)
        session.commit()


def insert_relation(relations: list):
    relation_model = [Relationship(student_id=int(relation['student_id']), class_id=relation['class_id'],
                                   teacher_id=relation['teacher_id'], enrollment_date=relation['enrollment_date'],
                                   relationship_type=relation['relationship_type']) for relation in relations]
    with session_maker() as session:
        session.add_all(relation_model)
        session.commit()