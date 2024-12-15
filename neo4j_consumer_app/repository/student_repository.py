from neo4j_consumer_app.db.database import driver


def insert_student(student: dict):
    try:
        with driver.session() as session:
            query = """
                create (s:Student $student)
                return c
            """
            params = {'student': student['id']}

            result = session.run(query, params).single()

            if result:
                return dict(result['s'])
            return None
    except Exception as e:
        print(f"Error inserting student: {e}")