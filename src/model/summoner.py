from neomodel import StructuredNode, StringProperty, IntegerProperty


class Summoner(StructuredNode):
    summoner_name = StringProperty(unique_index=True)
    summoner_id = StringProperty(unique_index=True)
    account_id = StringProperty(unique_index=True)
    summoner_level = IntegerProperty(unique_index=True)
    profile_icon_id = IntegerProperty()
