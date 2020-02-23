import datetime

import src.dao.riot_dao as riot_dao
import src.service.summoner_service as summoner_service
from src.model.game_instance import GameInstance
from src.model.summoner import Summoner


def get_match_history(summoner: Summoner, start_time: datetime, end_time: datetime):
    match_history = riot_dao.get_match_history_games(summoner, start_time, end_time)["matches"]
    for match_history_game in match_history:
        yield get_match(match_history_game["gameId"])


def get_match(match_id: str):
    return riot_dao.get_match(match_id)


def save_match(match_json: object):
    game_instance = GameInstance(
        game_id=match_json["gameId"],
        game_creation=match_json["gameCreation"],
        game_duration=match_json["gameDuration"],
        game_version=match_json["gameVersion"],
    ).save()

    summoner_participant_id_map = {}
    for participant_json in match_json["participantIdentities"]:
        summoner = summoner_service.get_summoner(participant_json["summonerName"])

        game_instance.goons.connect(summoner, {
            "champion": participant_json["championId"],
            "kills": participant_json["kills"],
            "assists": participant_json["assists"],
            "deaths": participant_json["deaths"],
            "first_blood_kill": participant_json["firstBloodKill"],
            "gold_earned": participant_json["goldEarned"],
            "total_damage_dealt_to_champions": participant_json["totalDamageDealtToChampions"]
        })
