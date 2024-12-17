from mongo_consumer_app.db.database import student_collection, review_collection, teacher_collection, class_collection, \
    relationship_collection


def insert_student(student: list):
    student_collection.insert_many(student)


def remove_field_student_id(dic: dict):
    dic.pop('student_id', None)
    return dic


def convert_life_style_to_float(life_style: dict):
    fields_to_convert = [ 'GPA', 'Sleep_Hours_Per_Day', 'Study_Hours_Per_Day',
        'Extracurricular_Hours_Per_Day', 'Social_Hours_Per_Day', 'Physical_Activity_Hours_Per_Day']

    for field in fields_to_convert:
        life_style[field] = float(life_style.get(field, 0))

    return life_style


def insert_life_style(life_styles: list):
    for life_style in life_styles:
        convert_life = convert_life_style_to_float(life_style)
        student_collection.update_one(
            {'id': convert_life['student_id']},
            {'$set': {'life_style': remove_field_student_id(convert_life)}}
        )


def convert_performance_to_float(performance: dict):
    fields_to_convert = ['current_grade', 'attendance_rate', 'assignments_completed', 'missed_deadlines',
            'participation_score', 'midterm_grade', 'study_group_attendance', 'office_hours_visits',
            'extra_credit_completed']

    for field in fields_to_convert:
        performance[field] = float(performance.get(field, 0))

    return performance


def insert_performance(performances: list):
    for performance in performances:
        convert_performance = convert_performance_to_float(performance)
        student_collection.update_one(
            {'id': convert_performance['student_id']},
            {'$set': {'performance': remove_field_student_id(convert_performance)}}
        )


def insert_review(review: list):
    review_collection.insert_many(review)


def insert_teacher(teacher: list):
    teacher_collection.insert_many(teacher)


def insert_class(class_: list):
    class_collection.insert_many(class_)


def insert_relationship(relation: list):
    relationship_collection.insert_many(relation)
