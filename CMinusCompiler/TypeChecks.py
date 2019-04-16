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
    if compare_node_value(node.value, ["<", "<=", ">=", ">", "+", "-", "*", "/", "="]):
        
        #print("CHECK: ", node.value)
        
        # Check that all of the children of this node are integers
        for child in node.children:
            if not typecheck(child, symbol_tables):
                return False        # A typecheck failed
        return True                 # All children typecheched successfully

    # Symbol table check
    var_properties = symbol_tables.lookup(node.value)
    if var_properties is not None:
        # Integer []
        if var_properties[0] == "int[]":
            if len(node.children)==0:
                print("ERROR: se esperaba int y se recibio int[] variable", node.value, "en", symbol_tables.scopeName)
                return False
        
            # 1 child (array with index)
            else:
                # Raw number index
                try: 
                    index = int(node.children[0].value)
                    if index >= int(var_properties[1]["size"]):
                        print("ERROR: indice", index, "fuera de rango en la variable", node.value,"en", symbol_tables.scopeName)
                        return False
                        
                # Check that variable inside is an int
                except ValueError:
                    return typecheck(node.children[0], symbol_tables)
        
    # None of the options listed above worked
    return False

# Helper function to check if value of the node is equal to at least one element in the array
def compare_node_value(node_value, values_array):
    for value in values_array:
        if node_value == value:
            return True
    return False
