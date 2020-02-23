import datetime

from neomodel import config

import src.service.summoner_service as summoner_service
from src.service import game_service
from src.util.definitions import NEO4J_URL

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
    print(summoner)

today = datetime.datetime.now()
lastMonth = today - datetime.timedelta(days=5)

i = 0
match_history = game_service.get_match_history(summoner_list[0], lastMonth, None)
for match_history_instance in match_history:
    game_service.save_match(match_history_instance)
    break
