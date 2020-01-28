import src.dao.riot_dao as riot_dao
from src.model.summoner import Summoner


def __initialize_summoner(summoner_name):
    """Create all necessary data structures needed for a new summoner object"""
    summoner_id = riot_dao.get_summoner_id(summoner_name)
    summoner = Summoner(summoner_id, summoner_name)

    return summoner


def get_summoner(summoner_name):
    return None
