from neomodel import config

import src.service.summoner_service as summoner_service
from src.util.definitions import NEO4J_URL

config.DATABASE_URL = NEO4J_URL
config.ENCRYPTED_CONNECTION = False
config.AUTO_INSTALL_LABELS = True

summoner_name_list = ["personmcpersons", "randomblackdude", "luckestt"]

for summoner_name in summoner_name_list:
    summoner_service.get_summoner(summoner_name)

summoner_list = summoner_service.get_summoner_list(summoner_name_list)

for summoner in summoner_list:
    print(summoner)
