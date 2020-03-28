import league_analytics_bot.util.definitions as definitions

with open(definitions.TOKEN_DIR + "/riot.token") as riot_token_file:
    RIOT_TOKEN = riot_token_file.read()

with open(definitions.TOKEN_DIR + "/discord.token") as discord_token_file:
    DISCORD_TOKEN = discord_token_file.read()