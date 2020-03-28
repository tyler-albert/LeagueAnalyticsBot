import sys

from league_analytics_bot.main.GIMP import GIMPClient
from league_analytics_bot.service import DISCORD_TOKEN


def print_usage():
    print("usage: python3 main.py [token file location]")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()

    client = GIMPClient()
    client.run(DISCORD_TOKEN)
