import random

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
    text = "These are not the droids you're looking for"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def board_poll_cmd(update: telegram.Update, bot):
    text = "Board poll"
    bot.send_poll(
        get_chat_id_from_update(update),
        question="Quin taulell voleu fer servir?",
        options=[
            "Clàssic",
            "Monstropolis",
            "Paris, La Belle Epoque",
            "1935 Atlantic City",
            "Snowdrop Valley",
        ],
        is_anonymous=False,
    )
    return success(text)


def get_shitty_offer_options():
    borderline_options = ["Borderline", "Meeeh...", "Més o menys", "D'aquella manera"]
    insulting_options = [
        "Pixada a la cara",
        "Insult",
        "Cómeme los huevos en copa",
        "Puto rastrero",
        "Rata de claveguera",
        "Luisal-level",
        "No tens honor",
    ]
    return ["No", random.choice(borderline_options), "Sí"] + random.sample(
        insulting_options, 2
    )


def shitty_offer_poll_cmd(update: telegram.Update, bot):
    text = "Mierdaoferta poll"
    bot.send_poll(
        get_chat_id_from_update(update),
        question="Mierdaoferta?",
        options=get_shitty_offer_options(),
        is_anonymous=False,
    )
    return success(text)
