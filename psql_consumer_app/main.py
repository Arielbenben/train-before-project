from psql_consumer_app.consumer import consume
from psql_consumer_app.db.database import init_tables



if __name__ == '__main__':
    init_tables()
    consume()
