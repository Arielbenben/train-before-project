from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from psql_consumer_app.db.models import Base
from psql_consumer_app.db.models.student import Student



class ReviewsStudents(Base):
    review_id = Column(Integer,primary_key=True, nullable=False)
    content = Column(String, nullable=False)
    score = Column(Integer, nullable=False)
    thumbs_up_count = Column(Integer, nullable=False)
    review_created_version = Column(String, nullable=False)
    date_time = Column(DateTime, nullable=False)
    app_version = Column(String, nullable=False)
    student_id = Column(Integer, ForeignKey(Student.id), nullable=False)
