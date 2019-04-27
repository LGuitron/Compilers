from SyntaxAnalyzer import SyntaxAnalyzer
from lexer import *


def parser(imprime = True):    
    syntax_analizer = SyntaxAnalyzer()
    AST = syntax_analizer.program()
    if imprime:
        print(AST)
    return AST
