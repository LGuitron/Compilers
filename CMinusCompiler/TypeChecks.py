# Helper function for performing typechecks for all corresponding nodes
# Return True if typecheck was successful
# Otherwise return False
def typecheck(node, symbol_tables):

    # Check for raw numbers
    try: 
        int(node.value)
        return True
    
    # Check other symbols
    except ValueError:
        pass
        
    # Operator check
    if compare_node_value(node.value, ["<", "<=", "==", "!=", ">=", ">", "+", "-", "*", "/", "="]):
        
        # Check that all of the children of this node are integers
        for child in node.children:
            if not typecheck(child, symbol_tables):
                return False        # A typecheck failed
        return True                 # All children typecheched successfully

    # Symbol table check
    var_properties = symbol_tables.lookup(node.value)
    if var_properties is not None:

        # Integer
        if var_properties[0] == "int":

            # Function
            if "params" in var_properties[1]:
        
                
                # Check that this name was called as a function                
                if len(node.children) > 0 and node.children[0].value == "_args":
                    
                    # Void function call
                    if var_properties[1]["params"] == "void":
                        if node.children[0].children[0].value == "void":
                            return True
                        else:
                            print("Error: la funcion", node.value,"() llamada en", symbol_tables.scopeName, "no recibe parametros")
                            return False                    
                    
                    # Check that the number of arguments is the same
                    if len (var_properties[1]["params"]) == len(node.children[0].children):
                        
                        success = True
                        for i in range(len(node.children[0].children)):
                            current_type = var_properties[1]["params"][i]
                            current_node = node.children[0].children[i]
                            
                            # Integer parameter validation
                            if current_type == "int":
                                
                                if not typecheck(current_node, symbol_tables):
                                    print("Error: ", current_node.value, "no es int")
                                    success = False
                            
                            # Integer[] validation 
                            elif current_type == "int[]":
                                
                                arr_properties = symbol_tables.lookup(current_node.value)
                                if arr_properties is not None:
                                    
                                    if arr_properties[0] != "int[]":
                                        print("Error: se esperaba int[] en el parametro", i, "en llamada a", node.value, "en", symbol_tables.scopeName)
                                        success = False
                                    
                                    # Error array received index, (so it is an int)
                                    elif len(current_node.children) > 0:
                                            print("Error: se esperaba int[] en el parametro", i, "en llamada a", node.value, "en", symbol_tables.scopeName)
                                            success = False
                                else:
                                    print("Error: int[]", current_node.value, "no fue declarado en llamada a", node.value, "en", symbol_tables.scopeName)
                                    success = False

                        return success
                    
                    # Error, numero de argumentos incorrecto
                    else:
                        print("Error: se esperaban" , len (var_properties[1]["params"]), "parametros, pero se recibieron", len(node.children[0].children), "en llamada a", node.value,"en",symbol_tables.scopeName)
                        return False
                
                else:
                    print("Error: ", node.value, "es una funcion, no una variable")
                    return False

            # Value
            else:
                
                # Check that the integer was called as variable and not as function
                if len(node.children) > 0 and node.children[0].value == "_args":
                    print("Error:", node.value, "es una variable y no puede ser llamada como funcion")
                    return False
                return True
        
        # Integer []
        elif var_properties[0] == "int[]":
            if len(node.children)==0:
                print("Error: se esperaba int y se recibio int[] variable", node.value, "en", symbol_tables.scopeName)
                return False
        
            # 1 child (array with index)
            else:
                # Raw number index
                try: 
                    index = int(node.children[0].value)
                    if index >= int(var_properties[1]["size"]):
                        print("Error: indice", index, "fuera de rango en la variable", node.value,"en", symbol_tables.scopeName)
                        return False
                        
                # Check that variable inside is an int
                except ValueError:
                    return typecheck(node.children[0], symbol_tables)
        
    # None of the options listed above worked
    print("Error:", node.value, "no es int")
    return False

# Helper function to check if value of the node is equal to at least one element in the array
def compare_node_value(node_value, values_array):
    for value in values_array:
        if node_value == value:
            return True
    return False
