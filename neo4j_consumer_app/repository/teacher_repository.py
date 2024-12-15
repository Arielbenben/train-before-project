from neo4j_consumer_app.db.database import driver


def insert_teacher(teacher: dict):
    try:
        with driver.session() as session:
            query = """
                create (t:Teacher $teacher)
                return t
            """
            params = {'teacher': teacher['id']}

            result = session.run(query, params).single()

            if result:
                return dict(result['t'])
            return None
    except Exception as e:
        print(f"Error inserting teacher: {e}")