from globalTypes import *
from lexer import *

f = open('sample.c-', 'r')
programa = f.read()             # lee todo el archivo a compilar
progLong = len(programa)        # longitud original del programa
programa = programa + '$'       # agrega un caracter $ que representa EOF
posicion = 0                    # posicion del caracter actual del string

# funcion para pasar los valores iniciales de las variables globales
globales(programa, posicion, progLong)
token, tokenString = getToken(True)
while (token != TokenType.ENDFILE):
    token, tokenString = getToken(True)
