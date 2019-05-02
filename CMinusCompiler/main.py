from globalTypes import *
from Parser import *
from semantica import *
from cgen import *

f = open('sample.c-','r')
programa = f.read() # lee todo el archivo a compilar
progLong = len(programa) # longitud original del programa 
programa = programa + '$' # agregar un caracter $ que represente EOF
posicion = 0 # posición del caracter actual del string

# función para pasar los valores iniciales de las variablesglobales
globales(programa, posicion, progLong)
AST = parser(False)
semantica(AST, False)
codeGen(AST, "file.asm")
