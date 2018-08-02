from fractions import Fraction
import music21 as m21
import sys

def convert_from_score(score):
    s = ''
    for part in score.parts:
        s += f'\\instrument<"piano">\n'
        s += '[ '
        for el in part.notes:
            if el.duration.quarterLength != 0.0:
                dur = 4 / Fraction(el.duration.quarterLength)

                # Single note
                if isinstance(el, m21.note.Note):
                    n = el.nameWithOctave
                # Chord
                elif isinstance(el, m21.chord.Chord):
                    n = '{'
                    for pitch in el.pitches:
                        n += pitch.nameWithOctave + ','
                    n += '}'
                
                # Add duration
                s += f"{n}*{dur.denominator}/{dur.numerator} "

        s += ' ]'
    return s

if __name__ == '__main__':
    score = m21.midi.translate.midiFilePathToStream(sys.argv[1])
    s = convert_from_score(score)
    print(s)
