# Ply used to generate the lexer for C-
import lex as lex


reserved = {
    'else'   : 'ELSE',
    'if'     : 'IF',
    'int'    : 'INT',
    'return' : 'RETURN',
    'void'   : 'VOID',
    'while'  : 'WHILE'
}
 
 
# List of token names.   This is always required
tokens = list(reserved.values()) + [
    'PLUS','MINUS','TIMES','DIVIDE', 'EQUALS',
    'LT','LE','GT','GE','EQ','NE',
    'SEMICOLON','COMMA',
    'LPAREN','RPAREN','LBRACKET','RBRACKET','LKEY','RKEY',
    'ID', 'NUM',
    'COMMENT',
    'ENDFILE'
]

# Assignment and aritmetic operators
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='

# Logical operators
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='

# coma and semicolon
t_COMMA     = r'\,'
t_SEMICOLON = r';'


# Grouping operators
t_LPAREN   = r'\('
t_RPAREN   = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY     = r'\{'
t_RKEY     = r'}'

# End of file
t_ENDFILE = r"\$"



# A regular expression rule with some action code
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)    
    return t


# return identifier with is value
def t_ID(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words 
    return t


def t_COMMENT(t):
    r'/\*( /* | \**[^*/])* \** \*/'
    t.value = str(t.value)
    t.lexer.lineno += t.value.count("\n")   # Add number of lines according to the amount of \n characters found
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return t
