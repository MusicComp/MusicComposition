import music21 as m21

###############################################################################
# Helpers and classes
###############################################################################

class MyPart():
    def __init__(self, instrument, els):
        self.instrument = instrument
        self.els = els

###############################################################################
# Lexer
###############################################################################
import ply.lex as lex
import re

tokens = (
        'SPACE',
        'INT',
        'PITCH',
        'REST',
        'TAG_INSTRUMENT',
        'TAG_TEMPO',
        'TAG_TIMESIGNATURE',
        'TAG_KEY',
        'STRING'
        )

t_SPACE = r'[ \t\n]+'

t_PITCH = r'[a-gA-G][#-]?[1-8]?'
t_REST = r'[r]'

# t_TAG = r'\\[a-zA-Z][a-zA-Z0-9_]*'
t_TAG_INSTRUMENT = r'\\instrument'
t_TAG_TEMPO = r'\\tempo'
t_TAG_TIMESIGNATURE = r'\\timesignature'
t_TAG_KEY = r'\\key'

def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'".*"'
    t.value = t.value[1:-1]
    return t

literals = [
        '/', '\\',
        '#', '-',
        '*',
        '%',
        '.', ',',
        '[', ']',
        '<', '>',
        '(', ')',
        '{', '}'
        ]

# Build lexer
lexer = lex.lex()

################################################################################
# Parser
################################################################################
import ply.yacc as yacc

def p_main(t):
    """
    main : part_list
    """
    t[0] = t[1]

def p_part_list(t):
    """
    part_list : 
              | part
              | part_list SPACE part
    """
    # empty
    if len(t) == 1:
        t[0] = []
    # single
    elif len(t) == 2:
        t[0] = [ t[1] ]
    else:
        t[0] = t[1]
        t[0].append(t[3])

def p_part(t):
    """
    part : '[' SPACE melody SPACE ']'
         | tag_instrument SPACE '[' SPACE melody SPACE ']'
    """
    if len(t) == 6:
        t[0] = MyPart('piano', t[5])
    else:
        t[0] = MyPart(t[1], t[5])

def p_melody(t):
    """
    melody : 
           | melody_element
           | melody SPACE melody_element
    """
    # empty
    if len(t) == 1:
        t[0] = []
    # single
    elif len(t) == 2:
        t[0] = [ t[1] ]
    else:
        t[0] = t[1]
        t[0].append(t[3])

def p_melody_element(t):
    """
    melody_element : note
                   | rest
                   | chord
                   | tag_tempo
                   | tag_timesignature
                   | tag_key
    """
    t[0] = t[1]

def p_note(t):
    """
    note : pitch duration
    """
    t[0] = m21.note.Note(t[1], duration=t[2])

def p_rest(t):
    """
    rest : REST duration
    """
    t[0] = m21.note.Rest(duration=t[2])

def p_chord(t):
    """
    chord : '{' chord_pitches '}'  duration
    """
    t[0] = m21.chord.Chord(t[2], duration=t[4])

def p_chord_pitches(t):
    """
    chord_pitches : 
                  | pitch
                  | chord_pitches ',' pitch
    """
    # empty
    if len(t) == 1:
        t[0] = []
    # single
    elif len(t) == 2:
        t[0] = [ t[1] ]
    else:
        t[0] = t[1]
        t[0].append(t[3])

def p_pitch(t):
    """
    pitch : PITCH
    """
    t[0] = m21.pitch.Pitch(t[1])

def p_duration_empty(t):
    "duration : "
    t[0] = m21.duration.Duration(quarterLength=1)

def p_duration_enum_denom(t):
    """
    duration : '*' enum '/' denom dotting
    """
    quarterLength = 4 * t[2] / t[4]
    dots = t[5]
    t[0] = m21.duration.Duration(quarterLength=quarterLength, dots=dots)


def p_duration_enum(t):
    """
    duration : '*' enum dotting
    """
    quarterLength = 4 * t[2]
    dots = t[3]
    t[0] = m21.duration.Duration(quarterLength=quarterLength, dots=dots)

def p_duration_denom(t):
    """
    duration : '/' denom dotting
    """
    quarterLength = 4 / t[2]
    dots = t[3]
    t[0] = m21.duration.Duration(quarterLength=quarterLength, dots=dots)

def p_enum(t):
    """
    enum : INT
    """
    t[0] = t[1]

def p_denom(t):
    """
    denom : INT
    """
    t[0] = t[1]

def p_dotting_none(t):
    "dotting : "
    t[0] = 0

def p_dotting_one(t):
    "dotting : '.'" # *3/2
    t[0] = 1

def p_dotting_two(t):
    "dotting : '.' '.'" # *7/4
    t[0] = 2

## def p_tag(t):
##     """
##     tag : '\\' tag_name
##         | '\\' tag_name '<' param_list '>'
##         | '\\' tag_name '(' note_series ')'
##         | '\\' tag_name '<' param_list '>' '(' note_series ')'
##     """

def p_tag_instrument(t):
    """
    tag_instrument : TAG_INSTRUMENT '<' STRING '>'
    """
    # https://github.com/cuthbertLab/music21/blob/master/music21/languageExcerpts/instrumentLookup.py
    t[0] = m21.instrument.fromString(t[3])

def p_tag_tempo(t):
    """
    tag_tempo : TAG_TEMPO '<' STRING '>'
              | TAG_TEMPO '<' INT '>'
    """
    t[0] = m21.tempo.MetronomeMark(t[3])

def p_tag_timesignature(t):
    """
    tag_timesignature : TAG_TIMESIGNATURE '<' STRING '>'
    """
    t[0] = m21.meter.TimeSignature(t[3])

def p_tag_key(t):
    """
    tag_key : TAG_KEY '<' STRING '>'
    """
    t[0] = m21.key.Key(t[3])

##
## def p_tag_id(t):
##     """
##     tag_name : 'instrument'
##              | 'key'
##              | 'meter'
##              | 'slur'
##     """
##
## param_list:
##     ''
##     param
##     param ',' param_list
## param: string

# Build parser
parser = yacc.yacc()

################################################################################
# Runner
################################################################################
import sys
import random

if __name__ == '__main__':
    input_str = sys.stdin.read().strip()
    ast = parser.parse(input_str)
    
    # Create score
    score = m21.stream.Score()
    
    # Create parts
    for p in ast:
        part = m21.stream.Part()
        # Add instrument 
        part.insert(p.instrument)
        for el in p.els:
            # Randomly adjust velocity (humanize)
            if isinstance(el, m21.note.Note) or isinstance(el, m21.chord.Chord):
                if not el.volume.velocity:
                    el.volume.velocity = 64
                el.volume.velocity += random.randint(0, 20)
                el.volume.velocity -= random.randint(0, 20)

            part.append(el)
        score.append(part)
    
    # Set tempo
    tm = m21.tempo.MetronomeMark(number=80)
    score.insert(0, tm)
    
    print(score.show('text'))
    
    # Play score
    score.show('midi')
