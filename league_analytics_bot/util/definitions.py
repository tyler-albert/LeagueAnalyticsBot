import os

PROJECT_ROOT = os.path.abspath("../")
TOKEN_DIR = PROJECT_ROOT + "/tokens"

NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "gimp"
NEO4J_HOST = "localhost"
NEO4J_PORT = "7687"
NEO4J_URL = "bolt://" + NEO4J_USERNAME + ":" + NEO4J_PASSWORD + "@" + NEO4J_HOST + ":" + NEO4J_PORT
