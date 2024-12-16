from mongo_consumer_app.db.database import student_collection, review_collection, teacher_collection, class_collection, \
    relationship_collection


def insert_student(student: list):
    student_collection.insert_many(student)


def insert_life_style(life_styles: list):
    for life_style in life_styles:
        student_collection.update_one(
            {'id': life_style['Student_ID']},
            {'$set': life_style}
        )

def insert_performance(performances: list):
    for performance in performances:
        student_collection.update_one(
            {'id': performance['student_id']},
            {'$set': performance}
        )


def insert_review(review: list):
    review_collection.insert_many(review)


def insert_teacher(teacher: list):
    teacher_collection.insert_many(teacher)


def insert_class(class_: list):
    class_collection.insert_many(class_)


def insert_relationship(relation: list):
    relationship_collection.insert_many(relation)