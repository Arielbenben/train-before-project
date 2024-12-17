from sqlalchemy import Integer, Column, ForeignKey, Float, String
from sqlalchemy.orm import relationship
from psql_consumer_app.db.models import Base



class LifeStyle(Base):
    __tablename__ = 'life_style'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'), nullable=False)
    Study_Hours_Per_Day = Column(Float, nullable=False)
    Extracurricular_Hours_Per_Day = Column(Float, nullable=False)
    Sleep_Hours_Per_Day = Column(Float, nullable=False)
    Social_Hours_Per_Day = Column(Float, nullable=False)
    Physical_Activity_Hours_Per_Day = Column(Float, nullable=False)
    GPA = Column(Float, nullable=False)
    Stress_Level = Column(String, nullable=False)

    student = relationship('Student', back_populates='life_style')
