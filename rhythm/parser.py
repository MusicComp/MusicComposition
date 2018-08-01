###############################################################################
# Classes
###############################################################################
class Note:
    def __init__(self, pitch, duration):
        self.pitch = pitch
        self.duration = duration
    def __str__(self):
        return f"[{self.pitch}, {self.duration}]"

class Pitch:
    def __init__(self, pitch_letter, octave):
        self.pitch_letter = pitch_letter
        self.octave = octave
    def __str__(self):
        return f"{self.pitch_letter}{self.octave}"

class Duration:
    def __init__(self, enum, denom):
        self.enum = enum
        self.denom = denom
    def __str__(self):
        return f"{self.enum}/{self.denom}"

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
        '#', 'b',
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
                | note SPACE note_series
    """
    # empty
    if len(t) == 1:
        t[0] = []
    # single
    elif len(t) == 2:
        t[0] = [ t[1] ]
    else:
        t[0] = [ t[1], t[3] ]

def p_note(t):
    """
    note : pitch duration
    """
    t[0] = Note(t[1], t[2])

def p_pitch_natural(t):
    """
    pitch : pitch_letter
          | pitch_letter octave
    """
    if len(t) == 2:
        octave = 4
    else:
        octave = t[2]
    t[0] = Pitch(t[1], octave)

def p_pitch_accidental(t):
    """
    pitch : pitch_letter accidental
          | pitch_letter accidental octave
    """
    if len(t) == 3:
        octave = 4
    else:
        octave = t[3]
    t[0] = Pitch(t[1] + t[2], octave)

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
               | 'b'
    """
    t[0] = t[1]

def p_octave(t):
    """
    octave : NUMBER
    """
    t[0] = t[1]

def p_duration_empty(t):
    "duration : "
    t[0] = Duration(1, 4)

def p_duration_denom(t):
    """
    duration : '/' denom
    """
    t[0] = Duration(1, t[2])

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
        s = input('> ')
    except EOFError:
        break
    notes = parser.parse(s)
    out = ''.join([str(n) for n in notes])
    print(out)
