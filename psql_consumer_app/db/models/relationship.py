from sqlalchemy import String, Column, ForeignKey
from psql_consumer_app.db.models import Base
from psql_consumer_app.db.models.student import Student
from psql_consumer_app.db.models.teacher import Teacher
from psql_consumer_app.db.models.class_ import Class


class Relationship(Base):
    student_id = Column(String, ForeignKey(Student.id), nullable=False)
    class_id = Column(String, ForeignKey(Class.id), nullable=False)
    teacher_id = Column(String, ForeignKey(Teacher.id), nullable=False)
    enrollment_date = Column(String, nullable=False)
    relationship_type = Column(String, nullable=False)

