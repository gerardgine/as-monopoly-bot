import telegram


def start_cmd(update: telegram.Update):
    text = "Hola, sóc el Fucking Monopoly Bot"
    update.message.reply_text(text)
    return text


def help_cmd(update: telegram.Update):
    text = "Comandes suportades:\n\n/taulell\n/mierdaoferta"
    update.message.reply_text(text)
    return text


def settings_cmd(update: telegram.Update):
    text = "These are not the androids you were looking for"
    update.message.reply_text(text)
    return text


def board_poll_cmd(update: telegram.Update):
    text = "Això hauria de crear una enquesta per triar el taulell"
    update.message.reply_text(text)
    return text


def shitty_offer_poll_cmd(update: telegram.Update):
    text = (
        "Això hauria de crear una enquesta per discutir com de merda és una "
        "oferta. Si és del Luisal, segur que ho és molt."
    )
    update.message.reply_text(text)
    return text
