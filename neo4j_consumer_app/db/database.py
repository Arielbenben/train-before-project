from neo4j import GraphDatabase
from neo4j_consumer_app.settings.neo4j_config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)