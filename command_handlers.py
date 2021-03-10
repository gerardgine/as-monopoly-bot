import random

import telegram

from responses import success


def get_chat_id_from_update(update: telegram.Update):
    return update.message.chat_id


def start_cmd(update: telegram.Update, bot):
    text = "Hola, sóc el Fucking Monopoly Bot"
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
            "Victorian London",
            "Cherry Blossom Tokyo",
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
        "Et pots fotre l'oferta pel cul",
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


def city_poll_cmd(update: telegram.Update, bot):
    text = "City poll"
    bot.send_poll(
        get_chat_id_from_update(update),
        question="Quina ciutat voleu fer servir amb el taulell clàssic?",
        options=[
            "Àustria - Austria",
            "Bòsnia - Bosnia",
            "Brasil - Brazil",
            "Canadà (FR) - Canada (FR)",
            "Croàcia - Croatia",
            "República Txeca - Czechia",
            "Dinamarca - Denmark",
            "Estònia - Estonia",
            "Finlàndia - Finland",
            "França - France",
            "Alemanya - Germany",
            "Hong Kong - Hong Kong",
            "Hongria - Hungary",
            "Índia - India",
            "Indonèsia - Indonesia",
            "Irlanda - Ireland",
            "Itàlia - Italy",
            "Amèrica Llatina - Latin America",
            "Letònia - Latvia",
            "Lituània - Lithuania",
            "Malàisia - Malaysia",
            "Mèxic - Mexico",
            "Països Baixos - Netherlands",
            "Noruega - Norway",
            "Polònia - Poland",
            "Portugal - Portugal",
            "Romania - Romania",
            "Rússia - Russia",
            "Sèrbia - Serbia",
            "Eslovàquia - Slovakia",
            "Eslovènia - Slovenia",
            "Sud-Àfrica - South Africa",
            "Espanya - Spain",
            "Espanya (català) - Spain (Catalan)",
            "Suècia - Sweden",
            "Suïssa (FR) - Switzerland (FR)",
            "Suïssa (DE) - Switzerland (DE)",
            "Turquia - Turkey",
            "Regne Unit - UK",
            "EUA - USA",
        ],
        is_anonymous=False,
    )
    return success(text)
