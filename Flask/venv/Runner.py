from flask import Flask, render_template
from Markov import *
import random

app = Flask(__name__)

keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

def createBaseMidi():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, random.choice(keys), 20)
    for chord in chords:
        score.append(chord)
    score.write('midi', 'static/midi/baseMidi.mid', status='replace')

def createLeftMidi():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, random.choice(keys), 20)
    for chord in chords:
        score.append(chord)
    score.write('midi', 'static/midi/leftMidi.mid', status='replace')

def createRightMidi():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, random.choice(keys), 20)
    for chord in chords:
        score.append(chord)
    score.write('midi', 'static/midi/rightMidi.mid', status='replace')

@app.route('/')
def index():
    createBaseMidi()
    createLeftMidi()
    createRightMidi()
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
