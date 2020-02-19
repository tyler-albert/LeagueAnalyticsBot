from neomodel import StructuredNode, StringProperty


class GameInstance(StructuredNode):
    platform_id = StringProperty()
    game_id = StringProperty()
