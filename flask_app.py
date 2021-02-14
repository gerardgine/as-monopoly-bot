import logging
# import telegram
from flask import Flask, jsonify, request

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
        app.logger.info("GET /")
        app.logger.info("request.args")
        app.logger.info(request.args)
        app.logger.info("request.form")
        app.logger.info(request.form)
        app.logger.info("request.values")
        app.logger.info(request.values)
        app.logger.info("request.json")
        app.logger.info(request.json)
        app.logger.info("request.data")
        app.logger.info(request.data)
        return "GET /"
    else:
        app.logger.info("POST /")
        app.logger.info("request.args")
        app.logger.info(request.args)
        app.logger.info("request.form")
        app.logger.info(request.form)
        app.logger.info("request.values")
        app.logger.info(request.values)
        app.logger.info("request.json")
        app.logger.info(request.json)
        app.logger.info("request.data")
        app.logger.info(request.data)
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
