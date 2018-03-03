from music21 import *
import random

def makeRelativeChord(_numeral, _key, _octave=4, _quarterLength=1):
    r = roman.RomanNumeral(_numeral)
    r.key = key.Key(_key)
    r.transpose(12 * (_octave-4), inPlace=True) # transpose octaves in place

    return chord.Chord(r.pitches, quarterLength=_quarterLength)

def makeChord(_sym, _octave):
    c = harmony.ChordSymbol(_sym, quarterLength=_quarterLength)

def canon():
    score = stream.Score()
    score.append(makeRelativeChord('I', 'D', 4))
    score.append(makeRelativeChord('V', 'D', 3))
    score.append(makeRelativeChord('vi', 'D', 3))
    score.append(makeRelativeChord('iii', 'D', 3))

    score.append(makeRelativeChord('IV', 'D', 3))
    score.append(makeRelativeChord('I', 'D', 3))
    score.append(makeRelativeChord('IV', 'D', 3))
    score.append(makeRelativeChord('V', 'D', 3))
    return score

# http://www.bsu.edu/libraries/beneficencepress/mathexchange/10-01/MarkovChainsChordProgressions.pdf
# romanNumerals = [ "I", "ii", "iii", "IV", "V", "vi", "viio" ] # Major
romanNumerals = [ 'i', 'iio', 'III', 'iv', 'v', 'VI', 'VII' ] # minor

# Mozart major
mozartMajorMC = [ [ 0, .13, 0, .15, .62, .05, .05 ],
        [ .49, 0, .01, 0, .40, .01, .09 ],
        [ .67, 0, 0, 0, 0, .33, 0 ],
        [ .64, .14, 0, 0, .15, 0, .07 ],
        [ .94, 0, 0, .01, 0, .04, .01 ],
        [ .11, .51, 0, .14, .20, 0, .04 ],
        [ .82, 0, .01, .01, .16, 0, 0 ] ]

bachMinor = [
    [ 0, .18, .01, .20, .41, .09, .12 ],
    [ .01, 0, .03, 0, .89, 0, .07 ],
    [ .06, .06, 0, .25, .19, .31, .13 ],
    [ .22, .14, 0, 0, .48, 0, .15 ],
    [ .80, 0, .02, .06, 0, .10, .02 ],
    [ .03, .54, .03, .14, .19, 0, .08 ],
    [ .81, 0, .01, .03, .15, 0, 0 ]
    ]

# https://www.reddit.com/r/touhou/comments/3scpu1/chord_progressions_in_touhou_music/
# TODO do real analysis on Touhou music
touhouZun = [
    [ 0.01, 0.01, 0.02, 0.02, 0.02, 0.9, 0.02 ], # i
    [ 0.9, 0.01, 0.01, 0.02, 0.02, 0.02, 0.02 ], # iio
    [ 0.9, 0.01, 0.01, 0.02, 0.02, 0.02, 0.02 ], # III
    [ 0.02, 0.02, 0.02, 0.01, 0.9, 0.01, 0.02 ], # iv
    [ 0.9, 0.02, 0.02, 0.02, 0.01, 0.01, 0.02 ], # v
    [ 0.02, 0.02, 0.02, 0.02, 0.01, 0.01, 0.9 ], # VI
    [ 0.9, 0.02, 0.02, 0.02, 0.02, 0.01, 0.01 ], # VII
    ]

rhythms = [
        [2, 2],
        [1, 1, 2],
        [2, 1, 1],
        [1, 1, 1, 1],
        [3, 1, 3, 1],
        ]

def generateChords(markov, _key, n):
    initial = 0 # I chord
    state = initial
    chords = [ makeRelativeChord(romanNumerals[initial], _key, _quarterLength=2) ]

    rhythmRow = 0
    rhythmCol = 0

    i = 0

    # Loop until last note is I
    while not(i >= n and state == 0):
        # Make probability space
        # TODO use counter?
        # https://stackoverflow.com/questions/14992521/python-weighted-random
        row = markov[state]
        probSpace = []
        for j in range(7):
            probSpace += [j] * int(row[j] * 100)

        # Get next state
        nextState = random.choice(probSpace)

        # Get duration from rhythm
        rhythm = rhythms[rhythmRow]
        # Get new rhythm if needed
        if rhythmCol >= len(rhythm):
            rhythmRow = random.randint(0, len(rhythms)-1)
            rhythmCol = 0
            rhythm = rhythms[rhythmRow]
        dur = rhythm[rhythmCol]
        rhythmCol += 1

        romanNumeral = romanNumerals[nextState]
        chord = makeRelativeChord(romanNumeral, _key, _quarterLength=dur)
        chords.append(chord)

        state = nextState

        i += 1

    return chords

def main():
    # score = canon()
    score = stream.Score()

    # chords = generateChords(mozartMajorMC, 'C', 20)
    chords = generateChords(bachMinor, 'Cm', 20)
    # chords = generateChords(touhouZun, 'Cm', 20)
    for chord in chords:
        score.append(chord)

    # midiFile = score.write('midi')
    # print(midiFile)
    midiFile = score.show('midi')

if __name__ == '__main__':
    main()
