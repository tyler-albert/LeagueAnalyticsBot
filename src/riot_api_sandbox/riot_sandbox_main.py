import requests
import src.dao.riot_dao as riot_dao

summoner_id = riot_dao.get_summoner_id("personmcpersons")
print(summoner_id)
