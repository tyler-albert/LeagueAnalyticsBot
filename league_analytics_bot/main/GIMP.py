from importlib import reload

import discord

import command_dispatcher


class GIMPClient(discord.Client):
    async def on_ready(self):
        print("Logged on as " + str(self.user))

    async def on_message(self, message):
        reload(command_dispatcher)
        if "reload" in message.content:
            print("reloaded")
            reload(command_dispatcher)
        else:
            command_dispatcher.on_message_handler(self, message)
