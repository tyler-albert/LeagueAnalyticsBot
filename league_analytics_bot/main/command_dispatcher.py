from discord import Message

from GIMP import GIMPClient


def on_message_handler(gimpstance: GIMPClient, message: Message):
    message_content = message.content

    print("Message 1: " + message.content + ", " + str(message.author))
