#  gTTS stands for Google Text To Speech, which is Googles text to speech API.
import gtts
import os
from playsound import playsound


def convert_to_audio(text=""):
    # make request to google to get synthesis
    tts = gtts.gTTS(text)

    # save the audio file
    tts.save("audio_response.mp3")

    # play the audio file
    sound = playsound("audio_response.mp3")
    os.remove('audio_response.mp3')
    return sound
