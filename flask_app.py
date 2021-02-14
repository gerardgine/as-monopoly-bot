import logging

from flask import abort, Flask, request

from commands import command_handler

app = Flask(__name__)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


@app.route("/", methods=["POST"])
def hello_world():
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

    if not request.json:
        abort(400)

    if get_message_type(request.json) == "bot_command":
        return command_handler(request.json)
    else:
        abort(400)


def get_message_type(data):
    try:
        return data["message"]["entities"][0]["type"]
    except KeyError:
        abort(400)
