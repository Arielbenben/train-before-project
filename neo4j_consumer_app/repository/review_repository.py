from neo4j_consumer_app.db.database import driver



def insert_review(review: dict):
    try:
        with driver.session() as session:
            query = """
                create (r:Review $review)
                return r
            """
            params = {'review': review['review_id']}

            result = session.run(query, params).single()

            if result:
                return dict(result['r'])
            return None
    except Exception as e:
        print(f"Error inserting review: {e}")