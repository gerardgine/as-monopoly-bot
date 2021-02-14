# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route("/start")
def start_cmd():
    return "Start"


@app.route("/help")
def help_cmd():
    return "Help"


@app.route("/settings")
def settings_cmd():
    return "Settings"
