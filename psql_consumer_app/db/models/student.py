from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from psql_consumer_app.db.models import Base




class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', age={self.age})>"

    life_style = relationship('LifeStyle', back_populates='student', uselist=False)
    performance = relationship('Performance', back_populates='student')
    reviews = relationship('ReviewsStudents', back_populates='student')
    relationships = relationship('Relationship', back_populates='student')

