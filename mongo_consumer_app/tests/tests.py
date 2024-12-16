import pytest



def test_mongo_connection(get_client):
    client = get_client
    try:
        client.admin.command("ping")
    except ConnectionError as e:
        pytest.fail(f"Failed to connect to MongoDB: {e}")