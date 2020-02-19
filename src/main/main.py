import sys

from src.main.GIMP import GIMPClient


def print_usage():
    print("usage: python3 main.py [token file location]")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()

    token_file = open(sys.argv[1], "r")
    token = token_file.readline()

    client = GIMPClient()
    client.run(token.strip())
