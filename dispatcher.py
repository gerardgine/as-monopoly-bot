import os

import telegram

from command_handlers import (
    start_cmd,
    help_cmd,
    settings_cmd,
    board_poll_cmd,
    shitty_offer_poll_cmd,
    city_poll_cmd,
)
from responses import success, error

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))
BOT_NAME = "FuckingMonopolyBot"


commands_to_command_handlers = {
    "start": start_cmd,
    "help": help_cmd,
    "settings": settings_cmd,
    "taulell": board_poll_cmd,
    "mierdaoferta": shitty_offer_poll_cmd,
    "ciutat": city_poll_cmd,
}


def strip_command_string(text: str):
    return_str = text
    if return_str.startswith("/"):
        return_str = return_str[1:]
    if return_str.endswith(f"@{BOT_NAME}"):
        return_str = return_str[: -len(f"@{BOT_NAME}")]
    return return_str


def dispatch(update: telegram.Update, bot: telegram.Bot):
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
    if not update.message:
        return success("Unsupported update type. Doing nothing.")

    bot_commands = update.message.parse_entities(telegram.MessageEntity.BOT_COMMAND)

    if not bot_commands:
        return success("Not a bot command. Doing nothing.")

    # Can there be more than 1 bot command on a single message?
    for entity, cmd_text in bot_commands.items():
        stripped_cmd = strip_command_string(cmd_text)
        if stripped_cmd in commands_to_command_handlers:
            response = commands_to_command_handlers[stripped_cmd](update, bot)
        else:
            return error(400, f"Invalid command: {cmd_text} (stripped: {stripped_cmd})")

    return response
