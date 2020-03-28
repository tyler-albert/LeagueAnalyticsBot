from math import pi as _pi

from model import Summoner


def create_pi_letter_indexes():
    pi = _pi
    letter_map = {}

    # while len(letter_map) < 26:
    # pi_value =


# pi_letter_indexes = create_pi_letter_indexes()
# print(pi_letter_indexes)


def _summoner_sort_cmp(value1: Summoner, value2: Summoner):
    return False


def summoner_sort(summoner_list: list):
    summoner_name_map = {}
    summoner_name_list = []
    for summoner in summoner_list:
        summoner_name_map[summoner.summoner_name] = summoner
        summoner_list.append(summoner.summoner_name)

    sorted_name_list = sorted(summoner_list, key=_summoner_sort_cmp)

    return_list = []
    for summoner_name in sorted_name_list:
        return_list.append(summoner_name_map[summoner_name])
