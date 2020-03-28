from neomodel import StructuredRel, IntegerProperty, BooleanProperty


class PlayedInRel(StructuredRel):
    champion = IntegerProperty()
    kills = IntegerProperty()
    assists = IntegerProperty()
    deaths = IntegerProperty()
    first_blood_kill = BooleanProperty()
    gold_earned = IntegerProperty()
    total_damage_dealt_to_champions = IntegerProperty()
