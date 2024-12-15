from elastic_consumer_app.db.database import elastic_client, review_index


def insert_review_to_elastic(review: dict):
    try:
        response = elastic_client.index(
            index=review_index,
            body=review
        )
        return response
    except Exception as e:
        return {'Error': str(e)}