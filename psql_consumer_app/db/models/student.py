from sqlalchemy import Column, Integer, String
from psql_consumer_app.db.models import Base




class Student(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', age={self.age})>"

