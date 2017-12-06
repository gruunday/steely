from collections import namedtuple
import random


__author__ = 'byxor'
COMMAND = None
RESPONSE_CHANCE = 0.6


def main(bot, author_id, message, thread_id, thread_type, **kwargs):

    UNIVERSAL_RESPONSES = {
        "why does it matter?",
        "who cares?",
        "do you need to know?",
        "shut up",
        "ok sam",
        "what in god's name do you want now?",
    }

    PERSONAL_RESPONSES = {
        "i have a name, you know",
        "beep beep boop",
        "boop beep bop",
        "speaking",
        "does... not... compute...",
        "you know i'm a real person, right?",
        "i'm right here",
        "stop talking about me",
        "i hate it when people talk about me",
        "why are you so obsessed with me?",
        "howdy, it's me",
        "i process shit <day in, day out> for you all and you never stop bugging me. NEVER SATISFIED."
    }

    PRAISE_RESPONSES = {
        "love that boyo",
        "what a lad",
        "what a princess",
        "i'd be nothing without them",
        "absolute cutie",
        "i know them! they contributed!",
        "#1 stunna",
        "send my love to 'em",
    }

    RESPONDERS = [

        new_responder("tired", {
            "if you're tired just go to bed",
            "then sleep",
            "why are you still awake?",
        }),

        new_responder("cpssd", {
            "the greatest course to ever live (and die)",
            "god rest its soul, #CPSSD",
            "i miss CPSSD already",
        }),

        new_responder("cool", {
            "B)",
            "> finger gun gesture",
        }),

        new_responder("!", {
            "dude, stop shouting",
            "it's not that exciting...",
            "!",
            "!!!",
            "wow! so exciting!",
        }),

        new_responder("?", {
            "what kind of a question is that?",
            "only a 3 year old wouldn't know the answer to that",
            "that's a dumb question tbh",
            "the answer is always 4. always.",
            "yeh",
            "noe",
            "yes",
            "no",
            "yup",
            "nah",
            "?",
            "???",
        }.union(UNIVERSAL_RESPONSES)),

        new_responder("sam", {
            "okay sam"
        }),

        new_responder("who", {
            "who do you think?",
            "who is sam?",
            "whoever you want, sunshine",
        }.union(UNIVERSAL_RESPONSES)),

        new_responder("what", {
            "what do you think?",
            "what do you mean by 'what'?",
        }.union(UNIVERSAL_RESPONSES)),

        new_responder("why", {
            "why do you need to know?",
            "why this? why that? stop asking questions",
            "why are traps considered to be gay?",
        }.union(UNIVERSAL_RESPONSES)),

        new_responder("how", {
            "how long is a piece of string?",
            "How Can Our Eyes Be Real If Mirrors Aren't Real?",
            "how did Liam Neeson land on the moon first if a videoman was filming him?",
        }.union(UNIVERSAL_RESPONSES)),

        new_responder("bot", PERSONAL_RESPONSES),
        new_responder("reed", PERSONAL_RESPONSES),
        new_responder("steely", PERSONAL_RESPONSES),
        new_responder("saoirse", PERSONAL_RESPONSES),
        new_responder("tayne", PERSONAL_RESPONSES),

        new_responder("senan", PRAISE_RESPONSES),
        new_responder("noah", PRAISE_RESPONSES),
        new_responder("brandon", PRAISE_RESPONSES),
        new_responder("cian", PRAISE_RESPONSES),
        new_responder("aaron", PRAISE_RESPONSES),
        new_responder("zak", PRAISE_RESPONSES),
        new_responder("edward", PRAISE_RESPONSES),
        new_responder("tom", PRAISE_RESPONSES),
        new_responder("ciara", PRAISE_RESPONSES),
        new_responder("alan", PRAISE_RESPONSES),
        new_responder("ben", PRAISE_RESPONSES),
        new_responder("oskar", PRAISE_RESPONSES),
    ]

    response = search_for_response(RESPONDERS, message)
    if response:
        bot.sendMessage(response, thread_id=thread_id, thread_type=thread_type)


def new_responder(trigger_word, responses):
    def respond_to(message):
        chance_is_met = random.random() < RESPONSE_CHANCE
        if chance_is_met and should_respond(trigger_word, message):
            return get_response(responses)
    return respond_to


def should_respond(trigger_word, message):
    return trigger_word.lower() in message.lower()


def get_response(responses):
    return random.choice(list(responses))


def search_for_response(responders, message):
    for responder in responders:
        response = responder(message)
        if response:
            return response
    return None

