import src.dao.riot_dao as riot_dao
from src.model.summoner import Summoner


def initialize_summoner(summoner_name):
    summoner_id = riot_dao.get_summoner_id(summoner_name)
    summoner = Summoner(summoner_id, summoner_name)

    return summoner
