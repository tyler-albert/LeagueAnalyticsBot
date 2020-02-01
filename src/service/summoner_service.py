import src.dao.riot_dao as riot_dao
from src.model.summoner import Summoner


def get_summoner(summoner_name):
    summoner = Summoner.nodes.get_or_none(summoner_name=summoner_name)
    if not summoner:
        summoner_id = riot_dao.get_summoner_id(summoner_name)
        summoner = Summoner(summoner_name=summoner_name, summoner_id=summoner_id).save()

    return summoner


def get_summoner_list(summoner_name_list):
    summoner_list = []
    for summoner_name in summoner_name_list:
        summoner_list.append(get_summoner(summoner_name))
    return summoner_list
