def on_message_handler(gimpstance, message):
    command_args = message.split(message)
    command = command_args[0]

    # if command == "predict":
