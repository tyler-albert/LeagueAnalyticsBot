from neomodel import StructuredNode, StringProperty


class Summoner(StructuredNode):
    summoner_name = StringProperty(unique_index=True)
    summoner_id = StringProperty(unique_index=True)
