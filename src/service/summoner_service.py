import src.dao.riot_dao as riot_dao
from src.model.summoner import Summoner

match_history_page_size = 50


def get_summoner(summoner_name):
    summoner = Summoner.nodes.get_or_none(summoner_name=summoner_name)
    if not summoner:
        riot_summoner = riot_dao.get_summoner_id(summoner_name)
        print(str(riot_summoner))
        summoner = Summoner(
            summoner_name=summoner_name,
            summoner_id=riot_summoner["id"],
            account_id=riot_summoner["accountId"],
            summoner_level=riot_summoner["summonerLevel"],
            profile_icon_id=riot_summoner["profileIconId"]
        ).save()

    return summoner


def get_summoner_list(summoner_name_list):
    summoner_list = []
    for summoner_name in summoner_name_list:
        summoner_list.append(get_summoner(summoner_name))
    return summoner_list


def get_match_history(summoner, start_time, end_time):
    return riot_dao.get_match_history_games(summoner, start_time, end_time)
