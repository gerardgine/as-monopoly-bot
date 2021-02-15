import logging
import os

from flask import abort, Flask, request
import telegram

from dispatcher import dispatch

SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def get_token():
    with open(os.path.join(SCRIPT_DIR, "auth_token"), "r") as fd:
        return fd.read().strip()


def authorize():
    try:
        return telegram.Bot(token=get_token())
    except telegram.error.InvalidToken:
        abort(401, "Invalid Telegram token")


app = Flask(__name__)
bot = authorize()


@app.route("/", methods=["POST"])
def root_url():
    app.logger.info(request.json)
    if not request.json:
        abort(400)

    update = telegram.Update.de_json(request.json, bot)
    return dispatch(update, bot)
