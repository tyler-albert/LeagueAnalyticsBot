from neomodel import StructuredNode, StringProperty


class DiscordUser(StructuredNode):
    username = StringProperty(unique_index=True)
