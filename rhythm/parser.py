import music21 as m21

###############################################################################
# Lexer
###############################################################################
import ply.lex as lex
import re

tokens = (
        'SPACE',
        'NUMBER',
        'LETTER',
        # 'ALPHANUM',
        )

t_SPACE = r'[ \t]'
t_LETTER = r'[a-zA-Z]'
# t_ALPHANUM = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

literals = [
        '/', '\\',
        '#', '-',
        '%',
        '.',
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
    main : note_series
    """
    t[0] = t[1]

def p_note_series(t):
    """
    note_series : 
                | note
                | note_series SPACE note
    """
    # empty
    if len(t) == 1:
        t[0] = m21.stream.Stream()
    # single
    elif len(t) == 2:
        t[0] = m21.stream.Stream()
        t[0].append(t[1])
    else:
        t[0] = t[1] # stream
        t[0].append(t[3])

def p_note(t):
    """
    note : pitch duration
    """
    t[0] = m21.note.Note(t[1], duration=t[2])

def p_pitch_natural(t):
    """
    pitch : pitch_letter
          | pitch_letter octave
    """
    if len(t) == 2:
        octave = 4
    else:
        octave = t[2]
    t[0] = m21.pitch.Pitch(t[1] + str(octave))

def p_pitch_accidental(t):
    """
    pitch : pitch_letter accidental
          | pitch_letter accidental octave
    """
    if len(t) == 3:
        octave = 4
    else:
        octave = t[3]
    t[0] = m21.pitch.Pitch(t[1] + t[2] + str(octave))

def p_pitch_letter(t):
    """
    pitch_letter : LETTER
    """
    if not re.match(r"[a-gA-G]", t[1]):
        raise yacc.YaccError("Invalid pitch letter")
    t[0] = t[1]

def p_accidental(t):
    """
    accidental : '#'
               | '-'
    """
    t[0] = t[1]

def p_octave(t):
    """
    octave : NUMBER
    """
    t[0] = t[1]

def p_duration_empty(t):
    "duration : "
    t[0] = m21.duration.Duration(0.25)

def p_duration_denom(t):
    """
    duration : '/' denom
    """
    t[0] = m21.duration.Duration(1.0 / t[2])

def p_denom(t):
    """
    denom : NUMBER
    """
    t[0] = t[1]

# TODO: enum, enum_denom, dottings...

# """
# duration : '*' enum '/' denom dotting
# duration : '*' enum dotting
# duration : '/' denom dotting
# """

def p_dotting_one(t):
    "dotting : '.'"
    t[0] = 1.5 # *3/2

def p_dotting_two(t):
    "dotting : '.' '.'"
    t[0] = 1.75 #* 7/4

## def p_tag(t):
##     """
##     tag : '\\' tag_name
##         | '\\' tag_name '<' param_list '>'
##         | '\\' tag_name '(' note_series ')'
##         | '\\' tag_name '<' param_list '>' '(' note_series ')'
##     """
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
while True:
    try:
        line = input('> ')
    except EOFError:
        break
    stream = parser.parse(line)
    print(stream)
    stream.show('midi')
