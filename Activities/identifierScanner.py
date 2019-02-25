current_state      = 1
current_identifier = '' 
error_state        = False
delimiters = {' ' , '\n' , '$'}



with open('identifierInput.txt') as f:
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
        
        if current_state == 1:
            if symbol.isalpha():
                current_state = 2
                current_identifier += symbol

            # ERROR
            elif symbol not in delimiters:
                print("ERROR: identificadores deben iniciar con una letra")
                current_identifier = ''
                error_state = True
                
        if current_state == 2:
            if symbol.isalpha or symbol.isdigit():
                current_state = 2
                if(symbol != '\n'):
                    current_identifier += symbol
        
            # ERROR
            else:
                print("ERROR: identificadores deben iniciar con una letra seguido de letras o numeros")
                current_identifier = ''
                error_state = True

            if symbol in delimiters:
                print("ID: " , current_identifier)
                current_identifier = ''
                current_state = 1

            
        if symbol == '$':
            exit()
