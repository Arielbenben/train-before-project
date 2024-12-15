from sqlalchemy import String, Column, Integer
from psql_consumer_app.db.models import Base


class Class(Base):
    id = Column(String, primary_key=True, nullable=False)
    course_name = Column(String, nullable=False)
    section = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    semester = Column(String, nullable=False)
    room = Column(String, nullable=False)
    schedule = Column(String, nullable=False)
    teacher_id = Column(String, nullable=False)
