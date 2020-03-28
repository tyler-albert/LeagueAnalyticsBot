import logging

from neomodel import config

from league_analytics_bot.service import summoner_service, game_service
from league_analytics_bot.util.definitions import NEO4J_URL

logging = logging.getLogger("gimp_logger")

config.DATABASE_URL = NEO4J_URL
config.ENCRYPTED_CONNECTION = False
config.AUTO_INSTALL_LABELS = True

summoner_name_list = [
    "personmcpersons",
    "randomblackdude",
    "luckestt",
    "LighttheJay",
    "Dînkleberg"
]

for summoner_name in summoner_name_list:
    summoner_service.get_summoner(summoner_name)

summoner_list = summoner_service.get_summoner_list(summoner_name_list)

for summoner in summoner_list:
    game_service.initialize_match_history(summoner)
