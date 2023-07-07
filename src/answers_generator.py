import json
import os
from pathlib import Path
import numpy as np
import pyttsx3

home_dir = Path(os.getcwd())
home_dir = str(home_dir.parent.absolute())

f = open(home_dir + "/generator_settings.json")
data = json.load(f)
f.close()
del f

number_of_questions = data["number_of_questions"]
note_range = data["note_range"]
interval_range = data["interval_range"]
del data

notes = np.genfromtxt("notes.csv", delimiter=',')

#TTS CLASS////////////////////////////////////////////////////////////
class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)  # Between 0 and 1

    def text_to_speech(self, text: str, file_name='output.mp3'):
        self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'({i + 1}) {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [ID: {voice.id}]')

tts = TextToSpeech(None, 200, 1.0)
        
def get_interval(note1, note2):
    intervals = ["unison", "flat two", "second", "minor third", "major third", "fourth", "tritone", "fifth",
              "minor sixth", "major sixth", "minor seventh", "major seventh", "octave", "flat nine", "ninth", 
              "flat ten", "tenth","eleventh", "sharp eleven", "twelfth", "flat thirteen", "thirteenth"]
    
    note1 = int(note1)
    note2 = int(note2)
  
    interval = intervals[ abs(note1 - note2) ]

    return interval


def get_answers_mp3():
    answers = ""

    for pair in range(notes.shape[0]):
        answers = answers + get_interval(notes[pair][0], notes[pair][1]) + "\n\n"

    tts.text_to_speech(answers, file_name='answers.mp3')


get_answers_mp3()