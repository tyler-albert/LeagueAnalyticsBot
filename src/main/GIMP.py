import discord


class GIMPClient(discord.Client):
    async def on_ready(self):
        print("Logged on as " + str(self.user))

    async def on_message(self, message):
        print("Message from " + str(message.author) + str(message.content))
