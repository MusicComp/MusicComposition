from fractions import Fraction
import music21 as m21

def convert_from_score(score):
    s = ''
    for part in score.parts:
        s += f'\\instrument<"piano">\n'
        s += '[ '
        for note in part.notes:
            if isinstance(note, m21.note.Note):
                if note.duration.quarterLength != 0.0:
                    dur = 4 / Fraction(note.duration.quarterLength)
                    n = note.nameWithOctave + '*' + str(dur.denominator) + '/' + str(dur.numerator)
                    s += n + ' '
                else:
                    # WTF?
                    pass
            # TODO handle chords
        s += ' ]'
    return s

if __name__ == '__main__':
    score = m21.midi.translate.midiFilePathToStream('broken_moon.mid')
    s = convert_from_score(score)
    print(s)
