import numpy as np

# Dictionary mapping symbol to corresponding index in table
symbols_dict = {'0':0, '1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,
                '+':1,'-':1,
                '.':2,
                'E':3,
                ' ':4, '\n':4, '$':4}     


# DFA table (8 states, and 5 possible readings)
table = np.array([
                 [2,7,0,0,1],
                 [2,0,3,4,8],
                 [3,0,0,4,8],
                 [6,5,0,0,0],
                 [6,0,0,0,0],
                 [6,0,0,0,8],
                 [2,0,0,0,0],
                ])

delimiters = {' ' , '\n' , '$'}

# Substract 1 to refer to indices (-1 is the error state)
table -= 1

current_state  = 0
current_number = '' 
error_state    = False  # Flag to determine actions when reaching error state

with open('numberInput.txt') as f:
    content = f.readlines()

for line in content:
    for symbol in line:        
        
        # Error Handling
        # When reaching error skip characters until next delimiter is found
        if error_state:
            if symbol in delimiters:
                error_state = False
            else:
                continue

        # Change state
        symbol_index  = symbols_dict[symbol]
        current_state   = table[current_state][symbol_index]   
        
        # Add last char into current number if they are not delimiters
        if symbol not in delimiters:
            current_number += str(symbol)                          
        
        # Solving errors when reaching the state -1
        if(current_state == -1):
            print("ERROR :" , current_number, " no es un numero valido")
            current_state  = 0
            current_number = ''
            error_state = True

        # When finding a delimiter print the current number and reset
        elif(current_state == 7):
            print("NUM: " , current_number)
            current_state  = 0
            current_number = ''
            
        # Exit when finding EOF char $
        if symbol == '$':
            exit()
