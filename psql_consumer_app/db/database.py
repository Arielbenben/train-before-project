from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from psql_consumer_app.settings.psql_config import DB_URL



engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)