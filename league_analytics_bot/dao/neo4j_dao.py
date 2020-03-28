from neomodel import config

from league_analytics_bot.util.definitions import NEO4J_URL


def initialize():
    config.DATABASE_URL = NEO4J_URL


def save_user(user):
    print(user)
