import datetime
import logging

from league_analytics_bot.dao import riot_dao
from league_analytics_bot.model import GameInstance, Summoner
from league_analytics_bot.service import summoner_service


def get_match_history(summoner: Summoner, start_time: datetime, end_time: datetime):
    match_history = riot_dao.get_match_history_games(summoner, start_time, end_time)["matches"]
    for match_history_game in match_history:
        yield get_match(match_history_game["gameId"])


def get_match(match_id: str):
    return riot_dao.get_match(match_id)


def initialize_match_history(summoner: Summoner):
    today = datetime.datetime.now()
    last_month = today - datetime.timedelta(days=5)

    i = 0
    match_history = get_match_history(summoner=summoner, start_time=last_month)
    for match_history_instance in match_history:
        save_match(match_history_instance)


def save_match(match_json: dict):
    game_id = match_json["gameId"]

    game_instance = GameInstance.nodes.first_or_none(game_id=game_id)
    if game_instance is not None:
        # Only create a game if it doesn't already exist
        logging.info("skipping creation of game: [game_id=\"%s\"", game_id)
        return

    game_instance = GameInstance(
        game_id=game_id,
        game_creation=match_json["gameCreation"],
        game_duration=match_json["gameDuration"],
        game_version=match_json["gameVersion"],
    ).save()

    for i in range(len(match_json["participantIdentities"])):
        participant_identity_json = match_json["participantIdentities"][i]
        summoner = summoner_service.get_summoner(participant_identity_json["player"]["summonerName"])

        participant_json = match_json["participants"][i]
        summoner.games.connect(game_instance, {
            "champion": participant_json["championId"],
            "kills": participant_json["stats"]["kills"],
            "assists": participant_json["stats"]["assists"],
            "deaths": participant_json["stats"]["deaths"],
            "first_blood_kill": participant_json["stats"]["firstBloodKill"],
            "gold_earned": participant_json["stats"]["goldEarned"],
            "total_damage_dealt_to_champions": participant_json["stats"]["totalDamageDealtToChampions"]
        })
