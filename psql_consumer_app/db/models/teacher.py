from tokenize import String
from sqlalchemy import Column
from psql_consumer_app.db.models import Base


class Teacher(Base):
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    title = Column(String, nullable=False)
    office = Column(String, nullable=False)
    email = Column(String, nullable=False)
