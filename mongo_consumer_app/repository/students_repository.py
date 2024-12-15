from mongo_consumer_app.db.database import student_collection


def insert_student(student: dict):
    student_collection.insert_one(student)


def insert_life_style(life_style: dict):
    student_collection.update_one(
        {'id': life_style['student_id']},
        {'$set': life_style}
    )

def insert_performance(performance: dict):
    student_collection.update_one(
        {'id': performance['student_id']},
        {'$set': performance}
    )