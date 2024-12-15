from neo4j_consumer_app.db.database import driver



def add_relationship(relationship: dict):
    try:
        with driver.session() as session:
            query = """
                create (r:Relationship $relationship)
                return c
            """
            params = {'relationship': relationship}

            result = session.run(query, params).single()

            if result:
                return dict(result['c'])
            return None
    except Exception as e:
        print(f"Error inserting class: {e}")