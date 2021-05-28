import speech_recognition as sr
import sounddevice as sd
import wavio


def record():
    fs = 44100  # Sample rate
    seconds = 5  # Duration of recording

    my_recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    # Wait until recording is finished
    sd.wait()
    # Save as an Mp3 file
    wavio.write('Recording.mp3', my_recording, fs, sampwidth=2)


def recognizer():
    # Recognizer() is the function used to recognize speech
    r = sr.Recognizer()

    recording = sr.AudioFile('Recording.mp3')

    # This uses the record() to capture data from our wav file "recording"
    with recording as source:
        # This is to help eliminate noise from your sound
        # r.adjust_for_ambient_noise(source)
        audio = r.record(source)

    # We use google API to recognise speech from an audio source
    return r.recognize_google(audio, language='en-CA')


def reply():
    text = recognizer()
    return text
