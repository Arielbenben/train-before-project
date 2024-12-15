from sqlalchemy import Column, Integer, ForeignKey, String, Float
from psql_consumer_app.db.models import Base
from psql_consumer_app.db.models.student import Student


class Performance(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    course_name = Column(String, nullable=False)
    current_grade = Column(Float, nullable=False)
    attendance_rate = Column(Float, nullable=False)
    assignments_completed = Column(Integer, nullable=False)
    missed_deadlines = Column(Integer, nullable=False)
    participation_score = Column(Float, nullable=False)
    midterm_grade = Column(Float, nullable=False)
    study_group_attendance = Column(Integer, nullable=False)
    office_hours_visits = Column(Integer, nullable=False)
    extra_credit_completed = Column(Integer, nullable=False)

