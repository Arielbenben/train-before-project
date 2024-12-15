from neo4j_consumer_app.db.database import driver


def insert_class(class_: dict):
    try:
        with driver.session() as session:
            query = """
                create (c:Class $class)
                return c
            """
            params = {'class': class_['id']}

            result = session.run(query, params).single()

            if result:
                return dict(result['c'])
            return None
    except Exception as e:
        print(f"Error inserting class: {e}")

