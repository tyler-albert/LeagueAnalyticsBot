import requests

from src.service.token_service import RIOT_TOKEN

region = "na1"
baseURL = "https://" + region + ".api.riotgames.com/lol"


def __riotGET(apiString):
    """Generic method for executing a REST call against a riot api"""
    return requests.get(baseURL + apiString + "?api_key=" + RIOT_TOKEN).json()


def get_summoner_id(summoner_name):
    riot_summoner = __riotGET("/summoner/v4/summoners/by-name/personmcpersons")
    return riot_summoner["accountId"]


def get_champion_mastery(summoner):
    mastery_summary = __riotGET("champion-mastery/v4/champion-masteries/by-summoner/" + summoner.id)
