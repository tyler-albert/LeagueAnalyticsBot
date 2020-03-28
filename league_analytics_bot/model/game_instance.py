from neomodel import StructuredNode, StringProperty, IntegerProperty, Relationship


class GameInstance(StructuredNode):
    game_id = StringProperty(unique_index=True)
    game_creation = IntegerProperty()
    game_duration = IntegerProperty()
    game_version = StringProperty()
    goons = Relationship("league_analytics_bot.model.Summoner", "PLAYED_IN")
