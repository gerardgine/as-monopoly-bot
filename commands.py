import os

from flask import abort
import telegram

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_token():
    with open(os.path.join(SCRIPT_DIR, "auth_token"), "r") as fd:
        return fd.read()


def command_handler(data):
    """
    Sample request data:

    {
        "update_id": 123456789,
        "message": {
            "message_id": 16,
            "from": {
                "id": 456789,
                "is_bot": false,
                "first_name": "John",
                "last_name": "Appleseed",
                "username": "johnapleseed",
                "language_code": "en"
            },
            "chat": {
                "id": 456789,
                "first_name": "John",
                "last_name": "Appleseed",
                "username": "johnapleseed",
                "type": "private"
            },
            "date": 1613296854,
            "text": "/start",
            "entities": [{"offset": 0, "length": 6, "type": "bot_command"}]
        }
    }

    """

    try:
        bot = telegram.Bot(token=get_token())
    except Exception as e:
        print(e)
        raise e

    command = data["message"]["text"].split()[0]
    if command == "/start":
        return start_cmd(data, bot)
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


def start_cmd(data, bot):
    bot.send_message(chat_id=data["message"]["chat"]["id"], text="Fuck Yeah!")
    return ""


def help_cmd(data):
    return "Help"


def settings_cmd(data):
    return "Settings"


def board_poll_cmd(data):
    return "Taulell"


def shitty_offer_poll_cmd(data):
    return "Mierdaoferta!!!"
