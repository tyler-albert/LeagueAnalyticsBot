from abc import ABC

from neomodel import StructuredNode, StringProperty, IntegerProperty, Relationship

from game_instance import GameInstance
from src.model.played_in_relationship import PlayedInRel


class Summoner(StructuredNode, ABC):
    summoner_name = StringProperty(unique_index=True)
    summoner_id = StringProperty(unique_index=True)
    account_id = StringProperty(unique_index=True)
    summoner_level = IntegerProperty(unique_index=True)
    profile_icon_id = IntegerProperty()
    games = Relationship(GameInstance, "PLAYED_IN", model=PlayedInRel)
