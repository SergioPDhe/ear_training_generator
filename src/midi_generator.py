import json
import os
from pathlib import Path
import numpy as np
import mido
from mido import MidiFile, Message, MidiTrack

home_dir = Path(os.getcwd())
home_dir = str(home_dir.absolute())

f = open(home_dir + "/generator_settings.json")
data = json.load(f)
f.close()
del f

notes = np.genfromtxt("output/notes.csv", delimiter=',')
notes = notes.astype(int)

mid = MidiFile()
track = MidiTrack()
already_added = []


for i,pair in enumerate(notes):         # Get the index and the note. Array must be int notes             

    track.append(Message('note_on',note = pair[0], velocity = 120,time = 5000))
    track.append(Message('note_on',note = pair[1], velocity = 120,time = 1000))
    
    track.append(Message('note_on',note = pair[0], velocity = 0,time = 2000))
    track.append(Message('note_on',note = pair[1], velocity = 0,time = 0))
    
mid.tracks.append(track)
mid.save("output/notes.mid")