from sqlalchemy import Column,String
from sqlalchemy.orm import relationship
from psql_consumer_app.db.models import Base




class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    office = Column(String, nullable=False)
    email = Column(String, nullable=False)

    classes = relationship('Class', back_populates='teacher')
    relationship = relationship('Relationship', back_populates='teacher')