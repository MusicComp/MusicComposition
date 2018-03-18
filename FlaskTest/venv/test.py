from flask import Flask, render_template
from Markov import *
import random

app = Flask(__name__)

def createMidi():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, 'Cm', 20)
    for chord in chords:
        score.append(chord)
    fp = score.write('midi', 'static/midi/createdMidi.mid', status='replace')

def createMidi2():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, 'B', 20)
    for chord in chords:
        score.append(chord)
    fp = score.write('midi', 'static/midi/createdMidi2.mid', status='replace')

def createMidi3():
    score = stream.Score()
    chords = generateChords(mozartMajorMC, 'G', 20)
    for chord in chords:
        score.append(chord)
    fp = score.write('midi', 'static/midi/createdMidi3.mid', status='replace')

@app.route('/')
def index():
    createMidi()
    return render_template("index.html")

@app.route('/secondQuestion')
def secondQuestion():
    createMidi2()
    return render_template("secondQuestion.html")

@app.route('/thirdQuestion')
def thirdQuestion():
    createMidi3()
    return render_template("thirdQuestion.html")

if __name__ == '__main__':
    app.run()
