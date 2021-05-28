# This chatter module is a replica of the util module from the nltk.chat.util library
# The converse() and respond() functions were  modified to work with this program properly.

# Natural Language Toolkit: Chatbot Utilities
#
# Copyright (C) 2001-2021 NLTK Project
# Authors: Steven Bird <stevenbird1@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT
#
# Based on an Eliza implementation by Joe Strout <joe@strout.net>,
# Jeff Epler <jepler@inetnebr.com> and Jez Higgins <jez@jezuk.co.uk>.


import re
import random
import sound_recognizer
# This is to convert the bot's response to audio
import text_to_audio


reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you",
}


class Chat(object):
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # Function to pattern match, and convert the bots response to audio
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"

                # resp = "Turv: " + resp

                # This is where the text response, is converted to audio
                sound = text_to_audio.convert_to_audio(resp)
                return sound

    # Function to hold a conversation with a chatbot
    def converse(self, quit="quit"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                # This is were the changes occured, from line 126 - 132
                print("Please speak (you have 5 seconds)...")
                # This is to record the users question
                sound_recognizer.record()
                print("Done recording, please wait...")
                # This is to convert the sound to text, and save in the user_input variable
                user_input = sound_recognizer.reply()
                print(f"user: ", user_input, "\n")
            except EOFError:
                print(user_input)
                print("EOFError")

            # Exception thrown, when the user says nothing or speaks faintly.
            except Exception:
                print("\nPlease re-record your message more clearly...")
                print("Goodbye...")

            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                # print response
                self.respond(user_input)
