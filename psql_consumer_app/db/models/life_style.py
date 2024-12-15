from sqlalchemy import Integer, Column, ForeignKey, Float, String
from psql_consumer_app.db.models import Base
from psql_consumer_app.db.models.student import Student



class LifeStyle(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
    Study_Hours_Per_Day = Column(Float, nullable=False)
    Extracurricular_Hours_Per_Day = Column(Float, nullable=False)
    Sleep_Hours_Per_Day = Column(Float, nullable=False)
    Social_Hours_Per_Day = Column(Float, nullable=False)
    Physical_Activity_Hours_Per_Day = Column(Float, nullable=False)
    GPA = Column(Float, nullable=False)
    Stress_Level = Column(String, nullable=False)
