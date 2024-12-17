from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from psql_consumer_app.db.models import Base





class Relationship(Base):
    __tablename__ = 'relationship'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    class_id = Column(String, ForeignKey('class.id'), nullable=False)
    teacher_id = Column(String, ForeignKey('teacher.id'), nullable=False)
    enrollment_date = Column(String, nullable=False)
    relationship_type = Column(String, nullable=False)

    student = relationship('Student', back_populates='relationships')
    class_ = relationship('Class', back_populates='relationship')
    teacher = relationship('Teacher', back_populates='relationship')

