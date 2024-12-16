import pytest
from pymongo import MongoClient


@pytest.fixture(scope="module")
def get_client():
    client = MongoClient('mongodb://172.19.191.59:27017')
    yield client
    client.close()