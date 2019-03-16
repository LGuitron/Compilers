from enum import Enum

class TokenType(Enum):
    # Reserved words
    ELSE        = 'else'
    IF          = 'if'
    INT         = 'int'
    RETURN      = 'return'
    VOID        = 'void'
    WHILE       = 'while'

    # Aritmetic operations
    PLUS        = '+'
    MINUS       = '-'
    TIMES       = '*'
    DIVIDE      = '/'
    EQUALS      = '='
    
    # Logical operators
    LT          = '<'
    LE          = '<='
    GT          = '>'
    GE          = '>='
    EQ          = '=='
    NE          = '!='

    # coma and semicolon
    COMMA       = ','
    SEMICOLON   = ';'
    
    # Grouping operators
    LPAREN      = '('
    RPAREN      = ')'
    LBRACKET    = '['
    RBRACKET    = ']'
    LKEY        = '{'
    RKEY        = '}'

    COMMENT     = 300
    ID          = 301
    NUM         = 302
    ERROR       = 303
    ENDFILE     = 304
