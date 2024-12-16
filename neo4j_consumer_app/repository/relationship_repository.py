from neo4j_consumer_app.db.database import driver


def add_relationships(relationships: list):
    results = []
    with driver.session() as session:
        for relationship in relationships:
            query = """
                 merge (s:Student_Id {student_id: $student_id})
                 merge (t:Teacher_Id {teacher_id: $teacher_id})
                 merge (c:Class_Id {class_id: $class_id})
                 merge (s) - [:studying] -> (c)
                 merge (t) - [:teaching] -> (c)
                 return s, t, c
             """

            params = {
                'student_id': relationship['student_id'],
                'teacher_id': relationship['teacher_id'],
                'class_id': relationship['class_id']
            }
            result = session.run(query, params).single()

            if result:
                results.append(dict(result['c']))
            else:
                results.append(None)

    return results
