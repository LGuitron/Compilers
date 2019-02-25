from cMinusPlyLexer import *
from globalTypes import *

def globales(prog, pos, long):
    global programa
    global posicion
    global progLong
    global lexer
    programa = prog
    posicion = pos
    progLong = long

    # Build the lexer here
    lexer = lex.lex()
    lexer.input(programa)

def getToken(imprime = True):

    lexer   = globals()['lexer']
    tok     = lexer.token()
    type_up = tok.type.upper()

    if imprime and type_up != "ERROR":
        print ("(" , TokenType[type_up], " , " , tok.value, ")")
    
    # Recuperacion de errores
    if type_up == 'ERROR':
        errorRecovery(lexer, tok, type_up)

    return TokenType[type_up], tok.value

# Function for lexer error recovery
def errorRecovery(lexer, tok, type_up):
    
    print("--------------------------------------------------------------------")
    
    # Print error token and the corresponding char
    print ("(" , TokenType[type_up], " , " , tok.value[0], ")")
    print("Linea ", lexer.__dict__['lineno'], ": ERROR, caracter inesperado")
    
    
    # Get position of the conflicting character in the current line
    current_position = tok.__dict__['lexpos'] 
    while lexer.__dict__['lexdata'][current_position] != "\n" and current_position:
        current_position -= 1

    if lexer.__dict__['lineno'] == 1:
        error_position = tok.__dict__['lexpos']
    else:
        error_position = tok.__dict__['lexpos'] - current_position - 1
    
    # Print error line
    error_line = lexer.__dict__['lexdata'].split("\n")[lexer.__dict__['lineno']-1]
    print(error_line)
    
    # Print ^ in the corresponding position
    if error_position == 0:
        print("^")
    else:
        print(" " * (error_position-1) , "^")
    print("--------------------------------------------------------------------")
    
