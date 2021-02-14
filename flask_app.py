import logging
# import telegram
from flask import Flask, request

app = Flask(__name__)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def get_token():
    with open("auth_token", "r") as fd:
        return fd.read()


@app.route("/", methods=["POST", "GET"])
def hello_world():
    # bot = telegram.Bot(token=get_token())
    if request.method == "GET":
        logging.log(logging.INFO, "GET /")
        logging.log(logging.INFO, request)
        return "GET /"
    else:
        logging.log(logging.INFO, "POST /")
        logging.log(logging.INFO, request)
        return "POST /"


@app.route("/start")
def start_cmd():
    return "Start"


@app.route("/help")
def help_cmd():
    return "Help"


@app.route("/settings")
def settings_cmd():
    return "Settings"
