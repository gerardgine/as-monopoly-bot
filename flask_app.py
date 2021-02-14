# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return "Hello from Flask (GET method)!"
    else:
        return "Hello from Flask (POST method)!"


@app.route("/start")
def start_cmd():
    return "Start"


@app.route("/help")
def help_cmd():
    return "Help"


@app.route("/settings")
def settings_cmd():
    return "Settings"
