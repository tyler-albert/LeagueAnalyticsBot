import requests

from src.service.token_service import RIOT_TOKEN

region = "na1"
base_url = "https://" + region + ".api.riotgames.com/lol"


def __riot_get(api_string):
    """Generic method for executing a REST call against a riot api"""
    return requests.get(base_url + api_string + "?api_key=" + RIOT_TOKEN).json()


def get_summoner_id(summoner_name):
    riot_summoner = __riot_get("/summoner/v4/summoners/by-name/personmcpersons")
    return riot_summoner["accountId"]


def get_champion_mastery(summoner):
    mastery_summary = __riot_get("champion-mastery/v4/champion-masteries/by-summoner/" + summoner.id)
