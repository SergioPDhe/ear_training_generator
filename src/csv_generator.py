import json
import os
from pathlib import Path
import numpy as np
from random import randint

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


def get_notes():
    note2 = -999

    while note2 < note_range[0] or note2 > note_range[1]:
        note1 = randint(note_range[0], note_range[1])

        interval = randint(interval_range[0],interval_range[1])
        note2 = note1 + interval

    return [[note1, note2]]


def get_notes_csv():
    notes = np.array([[0,0]])
    for n in range(number_of_questions):
        notes = np.append(notes, get_notes(),axis=0)

    notes = np.delete(notes,0,0)

    np.savetxt("notes.csv", notes, delimiter=',')


get_notes_csv()