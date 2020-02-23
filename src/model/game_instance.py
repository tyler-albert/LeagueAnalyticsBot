from abc import ABC

from neomodel import StructuredNode, StringProperty, IntegerProperty, Relationship

from src.model.played_in_relationship import PlayedInRel
from src.model.summoner import Summoner


class GameInstance(StructuredNode, ABC):
    game_id = IntegerProperty(unique_index=True)
    game_creation = IntegerProperty()
    game_duration = IntegerProperty()
    game_version = StringProperty()
    goons = Relationship(Summoner, "PLAYED_IN", model=PlayedInRel)
