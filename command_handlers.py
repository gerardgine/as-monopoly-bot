import math
import random

import telegram

from responses import success

MAX_POLL_OPTIONS = 10
CITIES = [
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
]
GROUPED_CITIES = {
    "Amèrica": [
        "Brasil - Brazil",
        "Canadà (FR) - Canada (FR)",
        "Amèrica Llatina - Latin America",
        "Mèxic - Mexico",
        "EUA - USA",
    ],
    "Àsia & Àfrica": [
        "Hong Kong - Hong Kong",
        "Índia - India",
        "Indonèsia - Indonesia",
        "Malàisia - Malaysia",
        "Rússia - Russia",
        "Sud-Àfrica - South Africa",
    ],
    "Europa": [
        "Àustria - Austria",
        "Bòsnia - Bosnia",
        "Croàcia - Croatia",
        "República Txeca - Czechia",
        "Dinamarca - Denmark",
        "Estònia - Estonia",
        "Finlàndia - Finland",
        "França - France",
        "Alemanya - Germany",
        "Hongria - Hungary",
        "Irlanda - Ireland",
        "Itàlia - Italy",
        "Letònia - Latvia",
        "Lituània - Lithuania",
        "Països Baixos - Netherlands",
        "Noruega - Norway",
        "Polònia - Poland",
        "Portugal - Portugal",
        "Romania - Romania",
        "Sèrbia - Serbia",
        "Eslovàquia - Slovakia",
        "Eslovènia - Slovenia",
        "Espanya - Spain",
        "Espanya (català) - Spain (Catalan)",
        "Suècia - Sweden",
        "Suïssa (FR) - Switzerland (FR)",
        "Suïssa (DE) - Switzerland (DE)",
        "Turquia - Turkey",
        "Regne Unit - UK",
    ],
}


def get_chat_id_from_update(update: telegram.Update):
    return update.message.chat_id


def start_cmd(update: telegram.Update, bot: telegram.Bot):
    text = "Hola, sóc el Fucking Monopoly Bot"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def help_cmd(update: telegram.Update, bot: telegram.Bot):
    text = "Comandes suportades:\n\n/taulell\n/mierdaoferta"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def settings_cmd(update: telegram.Update, bot: telegram.Bot):
    text = "These are not the droids you're looking for"
    bot.send_message(get_chat_id_from_update(update), text)
    return success(text)


def send_poll_with_split_options(
    update: telegram.Update,
    bot: telegram.Bot,
    poll_options: list,
    question: str,
    open_period: int = None,
    allows_multiple_answers: bool = False,
):
    """
    Having to do this sucks, big time, but Telegram limits the amount of options per
    poll to 10 (as of March 10th, 2021), so if our poll has too many options, we'll
    send multiple polls and hope each user doesn't vote in more than one of the polls...

    ¯\_(ツ)_/¯
    """
    options_count = len(poll_options)
    options_per_poll = (
        MAX_POLL_OPTIONS
        if options_count % MAX_POLL_OPTIONS != 1
        else MAX_POLL_OPTIONS - 1
    )
    current_batch = 1
    total_batches = math.ceil(options_count / options_per_poll)
    for i in range(0, options_count, options_per_poll):
        if total_batches == 1:
            updated_question = question
        else:
            updated_question = f"{question} ({current_batch}/{total_batches})"
        bot.send_poll(
            get_chat_id_from_update(update),
            question=updated_question,
            options=poll_options[i : min(options_count, i + options_per_poll)],
            is_anonymous=False,
            open_period=open_period,
            allows_multiple_answers=allows_multiple_answers,
        )
        current_batch += 1


def board_poll_cmd(update: telegram.Update, bot: telegram.Bot):
    text = "Board poll"
    boards = [
        "Clàssic",
        "Monstropolis",
        "Paris, La Belle Epoque",
        "1935 Atlantic City",
        "Snowdrop Valley",
        "Victorian London",
        "Cherry Blossom Tokyo",
    ]
    send_poll_with_split_options(
        update=update,
        bot=bot,
        poll_options=boards,
        question="Quin taulell voleu fer servir?",
        open_period=60,
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


def shitty_offer_poll_cmd(update: telegram.Update, bot: telegram.Bot):
    text = "Mierdaoferta poll"
    send_poll_with_split_options(
        update=update,
        bot=bot,
        poll_options=get_shitty_offer_options(),
        question="Mierdaoferta?",
        open_period=180,
    )
    return success(text)


def city_poll_cmd(update: telegram.Update, bot: telegram.Bot):
    """
    city_poll_cmd(...) and  grouped_cities_poll_cmd(...) are handlers for the same
    command. The difference is that the former just sends one big poll (split as
    needed), while the latter groups the cities (and the splits as needed).
    """
    text = "City poll"
    send_poll_with_split_options(
        update=update,
        bot=bot,
        poll_options=CITIES,
        question="Quina ciutat voleu fer servir amb el taulell clàssic?",
        open_period=60,
        allows_multiple_answers=True,
    )
    return success(text)


def grouped_cities_poll_cmd(update: telegram.Update, bot: telegram.Bot):
    """
    city_poll_cmd(...) and  grouped_cities_poll_cmd(...) are handlers for the same
    command. The difference is that the former just sends one big poll (split as
    needed), while the latter groups the cities (and the splits as needed).
    """
    text = "City poll"
    for continent, cities in GROUPED_CITIES.items():
        send_poll_with_split_options(
            update=update,
            bot=bot,
            poll_options=cities,
            question=f"Quina ciutat voleu fer servir amb el taulell clàssic? - {continent}",
            open_period=60,
            allows_multiple_answers=True,
        )
    return success(text)
