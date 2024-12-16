from elastic_consumer_app.db.database import elastic_client, review_index
from elasticsearch.helpers import bulk


def insert_review_to_elastic(reviews: list):
    actions = [
        {
            "_op_type": "index",
            "_index": review_index,
            "_source": review
        }
        for review in reviews
    ]

    try:
        success, failed = bulk(elastic_client, actions)
        if failed > 0:
            return {'Error': f'Failed to insert {failed} reviews'}
        return {'Success': f'Inserted {success} reviews'}
    except Exception as e:
        return {'Error': f'Exception occurred: {str(e)}'}

def get_data():
    try:
        response = elastic_client.search(index=review_index, body={"query": {"match_all": {}}}, size=10000)  # Adjust size for your needs
        reviews = [doc["_source"] for doc in response["hits"]["hits"]]
        return reviews
    except Exception as e:
        raise RuntimeError(f"Error fetching data from index '{review_index}': {e}")
print(get_data())