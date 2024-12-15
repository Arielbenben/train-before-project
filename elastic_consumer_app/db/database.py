from elasticsearch import Elasticsearch


elastic_client = Elasticsearch(
    hosts=["http://localhost:9200"]
)
try:
    info = elastic_client.info()
except Exception as e:
    print(f"Failed to connect to Elasticsearch: {e}")


review_index = 'review'