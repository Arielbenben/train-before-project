from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from psql_consumer_app.db.models import Base
from psql_consumer_app.db.models.student import Student
from psql_consumer_app.db.models.teacher import Teacher
from psql_consumer_app.db.models.class_ import Class



class Relationship(Base):
    __tablename__ = 'relationship'

    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    class_id = Column(String, ForeignKey('class.id'), nullable=False)
    teacher_id = Column(String, ForeignKey('teacher.id'), nullable=False)
    enrollment_date = Column(String, nullable=False)
    relationship_type = Column(String, nullable=False)

    student = relationship('Student', back_populates='relationships')
    class_ = relationship('Class', back_populates='relationship')

