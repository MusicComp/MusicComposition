from music21 import *
import random

def makeRelativeChord(_numeral, _key, _octave=4, _quarterLength=1):
    r = roman.RomanNumeral(_numeral)
    r.key = key.Key(_key)
    r.transpose(12 * (_octave-4), inPlace=True) # transpose octaves in place
    return chord.Chord(r.pitches, quarterLength=_quarterLength)

def findInversion(_initialState, _nextState, _currentInversion):
    if _currentInversion == 0:
        return inv1[_initialState][_nextState]
    elif _currentInversion == 1:
        return inv2[_initialState][_nextState]
    elif _currentInversion == 2:
        return inv3[_initialState][_nextState]
    
    
def invertChord(_chord, _inversion):
    a = _chord.inversion(_inversion)
    
def makeChord(_sym, _octave):
    c = harmony.ChordSymbol(_sym, quarterLength=_quarterLength)

def allChords(var, cMa):
    cMa = chord.Chord("C4", "E4", "G4")
    cMb = chord.Chord("E4", "G4","C5")
    cMc = chord.Chord("G4", "C5", "E5")
    cShMa = chord.Chord("C#4", "F4", "G#4")
    cShMb = chord.Chord("F4", "G#4", "C#5")
    cShMc = chord.Chord("G#4", "C#5", "F5")
    dMa = chord.Chord("D4", "F#4", "A4")
    dMb = chord.Chord("F#4", "A4", "D5")
    dMc = chord.Chord("A4", "D5", "F#5")
    eMa = chord.Chord("E4", "G#4", "B4")
    eMb = chord.Chord("G#4", "B4", "E5")
    eMc = chord.Chord("B4", "E5", "G#5")
    fMa = chord.Chord("F4", "A4", "C5")
    fMb = chord.Chord("A4", "C5", "F5") 
    fMc = chord.Chord("C4", "F4", "A4")
    fShMa = chord.Chord("F#4", "A#4", "C#5")
    fShMb = chord.Chord("A#4", "C#5", "F#5")
    fShMc = chord.Chord("C#4", "F#4", "A#4")
    gMa = chord.Chord("G4", "B4", "D5")
    gMb = chord.Chord("B4", "D5", "G5")
    gMc = chord.Chord("D4", "G4", "B4")
    aFlMa = chord.Chord("A-4", "C5", "E-5")
    aFlMb = chord.Chord("C4", "E-4", "A-4")
    aFlMc = chord.Chord("E-4", "A-4", "C5")
    aMa = chord.Chord("A4", "C#5", "E5")
    aMb = chord.Chord("C#4", "E4", "A4")
    aMc = chord.Chord("E4", "A4", "C#5")
    bFlMa = chord.Chord("B-3", "D4", "F4")
    bFlMb = chord.Chord("D4", "F4", "B-4")
    bFlMc = chord.Chord("F4", "B-4", "D5")
    bMa = chord.Chord("B3", "D#4", "F#4")
    bMb = chord.Chord("D#4", "F#4", "B4")
    bMc = chord.Chord("F#4", "B4", "D#5")

def inversionMatrix():
    I = [ 'ii', 'iiic', 'IVc', 'Vb', 'vib', 'vii' ]
    Ib = [ 'iib', 'iii', 'IV', 'V', 'vic', 'viic' ]
    Ic = [ 'iic', 'iiib', 'IV', 'V', 'vi', 'vii' ]
    ii = [ 'I', 'iii', 'IVc', 'Vc', 'vib', 'viib' ]    
    iib = [ 'Ib', 'iiib', 'IV', 'V', 'vi', 'viic' ]
    iic = [ 'Ic', 'iiic', 'IVb', 'V', 'vi', 'vii' ] 
    iii = [ 'Ib', 'ii', 'IV', 'Vc', 'vib', 'viib' ]
    iiib = [ 'Ic', 'iib', 'IVb', 'V', 'vi', 'viic' ]
    iiic = [ 'I', 'iic', 'IVc', 'Vb', 'vib', 'vii' ]
    IV = [ 'Ib', 'iib', 'iii', 'V', 'vic', 'viic' ]
    IVb = [ 'Ic', 'iic', 'iiib', 'Vb', 'vi', 'vii' ]
    IVc = [ 'I', 'ii', 'iiic', 'Vc', 'vib', 'viib' ]
    V = [ 'Ic', 'iib', 'iiib', 'IV', 'vi', 'viic' ]
    Vb = [ 'I', 'ii', 'iiic', 'IVb', 'vib', 'vii' ]
    Vc = [ 'Ib', 'ii', 'iii', 'IV', 'vic', 'viib' ]
    vi = [ 'Ic', 'iib', 'iii', 'iiic', 'V', 'vii' ]
    vib = [ 'I', 'ii', 'iiic', 'iiic', 'Vc', 'viic' ]
    vic = [ 'Ib', 'iib', 'iii', 'iiic', 'Vc', 'viic' ]
    vii = [ 'Ic', 'iic', 'iiic', 'iiic', 'Vb', 'vi' ]
    viib = [ 'Ib', 'ii', 'iii', 'iiic', 'Vc', 'vib' ]
    viic = [ 'Ib', 'ii', 'iii', 'iiic', 'V', 'vib' ]

    all = [I, Ib, ic, ii, iib, iic, iii, iiib, iiic, IV, IVb, IVc, V, Vb, Vc, vi, vib, vic, vii, viib, viic]

# http://www.bsu.edu/libraries/beneficencepress/mathexchange/10-01/MarkovChainsChordProgressions.pdf
romanNumerals = [ "I", "ii", "iii", "IV", "V", "vi", "vii" ] # Major
# romanNumerals = [ 'i', 'iio', 'III', 'iv', 'v', 'VI', 'VII' ] # minor

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

inv1 = [
    [ 0, 0, 2, 2, 1, 1, 0 ],
    [ 0, 0, 0, 2, 2, 1, 1 ],   
    [ 2, 0, 0, 0, 2, 1, 1 ],
    [ 2, 2, 0, 0, 0, 2, 2 ],
    [ 2, 1, 1, 0, 0, 0, 2 ],
    [ 2, 1, 0, 2, 0, 0, 0 ],
    [ 2, 2, 2, 2, 1, 0, 0 ],
    ]

inv2 = [
    [ 0, 1, 0, 0, 0, 2, 2 ],
    [ 1, 0, 1, 0, 0, 0, 2 ],
    [ 2, 1, 0, 1, 0, 0, 2 ],
    [ 2, 2, 1, 0, 1, 0, 0 ],
    [ 0, 0, 2, 1, 0, 1, 0 ],
    [ 0, 0, 2, 2, 2, 0, 2 ],
    [ 1, 0, 0, 2, 2, 1, 0 ],
    ]


inv3 = [
    [ 0, 2, 1, 0, 0, 0, 0 ],
    [ 2, 0, 2, 1, 0, 0, 0 ],
    [ 0, 2, 0, 2, 1, 1, 0 ],
    [ 0, 0, 2, 0, 2, 1, 1 ],
    [ 1, 0, 0, 0, 0, 2, 1 ],
    [ 1, 1, 0, 2, 2, 0, 2 ],
    [ 1, 0, 0, 2, 0, 1, 0 ],
    ]
    
def generateChords(markov, _key, n):
    initial = 0 # I chord
    inversion = 0
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

        # From State --> nextState
        inversion = findInversion(state, nextState, inversion)
        
        romanNumeral = romanNumerals[nextState]
        chord = makeRelativeChord(romanNumeral, _key, _quarterLength=dur)
        invertChord(chord, inversion)
        
        chords.append(chord)

        state = nextState

        i += 1

    return chords

def main():
    score = stream.Score()
 
    # Creates the Score
    chords = generateChords(bachMinor, 'Cm', 20)
    for chord in chords:
        score.append(chord)
 
    # Creates the Midi
    fp = score.write('midi', 'Jon.mid')
    midiFile = score.show('midi')
 
    # Plays the Score
    sp = midi.realtime.StreamPlayer(score)
    sp.play()
    
if __name__ == '__main__':
    main()
