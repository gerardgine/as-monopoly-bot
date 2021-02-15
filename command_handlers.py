import telegram

from responses import success


def get_chat_id_from_update(update: telegram.Update):
    return update.message.chat_id


def start_cmd(update: telegram.Update, bot):
    text = "Hola, sóc el Fucking Monopoly Bot"
    # update.message.reply_text(text)
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def help_cmd(update: telegram.Update, bot):
    text = "Comandes suportades:\n\n/taulell\n/mierdaoferta"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def settings_cmd(update: telegram.Update, bot):
    text = "These are not the androids you were looking for"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def board_poll_cmd(update: telegram.Update, bot):
    text = "Això hauria de crear una enquesta per triar el taulell"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def shitty_offer_poll_cmd(update: telegram.Update, bot):
    text = (
        "Això hauria de crear una enquesta per discutir com de merda és una "
        "oferta. Si és del Luisal, segur que ho és molt."
    )
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)
