import datetime

import requests

from src.model.summoner import Summoner
from src.service.token_service import RIOT_TOKEN

region = "na1"
base_url = "https://" + region + ".api.riotgames.com/lol"


def __riot_get(api_string):
    """Generic method for executing a REST call against a riot api"""
    delimiter = "?"
    if "?" in api_string:
        delimiter = "&"

    full_url = base_url + api_string + delimiter + "api_key=" + RIOT_TOKEN
    print("request: " + full_url)

    return requests.get(full_url).json()


def get_summoner_id(summoner_name):
    riot_summoner = __riot_get("/summoner/v4/summoners/by-name/" + summoner_name)
    return riot_summoner


def get_champion_mastery(summoner):
    mastery_summary = __riot_get("champion-mastery/v4/champion-masteries/by-summoner/" + summoner.id)


def get_match_history_games(summoner: Summoner, start_time: datetime, end_time: datetime):
    request_string = "/match/v4/matchlists/by-account/" + summoner.account_id \
                     + "?beginTime=" + str(int(start_time.timestamp() * 1000))
    if end_time is not None:
        request_string += "&endTime=" + str(int(end_time.timestamp() * 1000))

    return __riot_get(request_string)
