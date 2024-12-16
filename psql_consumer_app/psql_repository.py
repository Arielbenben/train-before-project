from psql_consumer_app.db.database import session_maker
from psql_consumer_app.db.models.class_ import Class
from psql_consumer_app.db.models.life_style import LifeStyle
from psql_consumer_app.db.models.performance import Performance
from psql_consumer_app.db.models.relationship import Relationship
from psql_consumer_app.db.models.reviews_students import ReviewsStudents
from psql_consumer_app.db.models.student import Student
from psql_consumer_app.db.models.teacher import Teacher


def insert_student(student: dict):
    student_model = Student(**student)
    with session_maker() as session:
        session.add(student_model)
        session.commit()


def insert_life_style(life_style: dict):
    life_style_model = LifeStyle(**life_style)
    with session_maker() as session:
        session.add(life_style_model)
        session.commit()


def insert_performance(performance: dict):
    performance_model = Performance(**performance)
    with session_maker() as session:
        session.add(performance_model)
        session.commit()


def insert_review(review: dict):
    review_model = ReviewsStudents(**review)
    with session_maker() as session:
        session.add(review)
        session.commit()


def insert_teacher(teacher: dict):
    teacher_model = Teacher(**teacher)
    with session_maker() as session:
        session.add(teacher_model)
        session.commit()


def insert_class(class_: dict):
    class_model = Class(**class_)
    with session_maker() as session:
        session.add(class_model)
        session.commit()


def insert_relation(relation: dict):
    relation_model = Relationship(**relation)
    with session_maker() as session:
        session.add(relation_model)
        session.commit()