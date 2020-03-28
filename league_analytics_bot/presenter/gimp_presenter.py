import league_analytics_bot.service.riot_service as riot_service


def get_summoner(summoner_name):
    summoner = riot_service.get_summoner(summoner_name)
