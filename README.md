# Fucking Monopoly Bot
Simple Telegram bot for Monopoly games

## Local set up

Create virtualenv:
```shell
python3 -m venv venv
```

Activate virtualenv:
```shell
source venv/bin/activate
```

Upgrade pip:
```shell
pip install -U pip
```

Install requirements:
```shell
pip install -r requirements.txt
```

Start local development server:
```shell
FLASK_APP=flask_app.py FLASK_ENV=development flask run
```

## Useful links

### Telegram API
https://core.telegram.org/bots
https://core.telegram.org/bots#commands
https://core.telegram.org/bots/api#available-types
https://core.telegram.org/bots/api#getting-updates
https://core.telegram.org/bots/samples

### Python library
https://github.com/python-telegram-bot/python-telegram-bot
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-–-Your-first-Bot
https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks

### Flask
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request

### Hosting
https://www.pythonanywhere.com
