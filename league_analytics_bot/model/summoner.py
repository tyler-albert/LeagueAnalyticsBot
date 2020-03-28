from neomodel import StructuredNode, StringProperty, IntegerProperty, Relationship, DateProperty

from league_analytics_bot.model import PlayedInRel


class Summoner(StructuredNode):
    summoner_name = StringProperty(unique_index=True)
    summoner_id = StringProperty(unique_index=True)
    account_id = StringProperty(unique_index=True)
    summoner_level = IntegerProperty(unique_index=True)
    profile_icon_id = IntegerProperty()
    last_match_history_update = DateProperty()
    games = Relationship("league_analytics_bot.model.GameInstance", "PLAYED_IN", model=PlayedInRel)
