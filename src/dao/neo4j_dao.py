from neomodel import config

from src.util.definitions import NEO4J_URL


def initialize():
    config.DATABASE_URL = NEO4J_URL


def save_user(user):
    print(user)
