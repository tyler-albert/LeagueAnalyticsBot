admin_users = ["personmcperson"]


def is_admin(summoner):
    """Make a broad admin role that can modify other people's stuff"""
    return summoner.summoner_name in admin_users
