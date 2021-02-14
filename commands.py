from flask import abort
import telegram


def get_token():
    with open("auth_token", "r") as fd:
        return fd.read()


def command_handler(data):
    # bot = telegram.Bot(token=get_token())

    command = data["message"]["text"].split()[0]
    if command == "/start":
        return start_cmd(data)
    elif command == "/help":
        return help_cmd(data)
    elif command == "/settings":
        return settings_cmd(data)
    elif command == "/board" or command == "/taulell":
        return board_poll_cmd(data)
    elif command == "/mierdaoferta":
        return shitty_offer_poll_cmd(data)
    else:
        abort(400)


def start_cmd(data):
    return "Start"


def help_cmd(data):
    return "Help"


def settings_cmd(data):
    return "Settings"


def board_poll_cmd(data):
    return "Taulell"


def shitty_offer_poll_cmd(data):
    return "Mierdaoferta!!!"
