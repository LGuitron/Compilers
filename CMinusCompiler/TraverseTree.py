class TraverseTree:
    
    def __init__(self):
        self.scope_num      = 0
        self.error_detected = False
    
    def traverse(self, node, symbol_tables):
        self.scope_num = 0
        self.check_node(node, symbol_tables)
        return self.error_detected
        
    # Helper function for traversing the tree
    def check_node(self, node, symbol_tables):

        # Change scope to the funcion scope, and add value of function_num
        if node.value == "fun_declaration":
            if symbol_tables.parentTable is not None:
                symbol_tables = symbol_tables.parentTable
            symbol_tables = symbol_tables.childTables[self.scope_num]
            self.scope_num += 1
        
        # Check if the node has a value that needs to be typecheched
        if self.compare_node_value(node.value, ["<", "<=", ">=", ">", "+", "-", "*", "/", "="]):
            self.typecheck(node, symbol_tables)
        
        for child in node.children:
            self.check_node(child, symbol_tables)
        
    # Helper function for performing typechecks for all corresponding nodes
    # Return True if typecheck was successful
    # Otherwise return False
    def typecheck(self, node, symbol_tables):

        # Check for raw numbers
        try: 
            int(node.value)
            return True
        
        # Check other symbols
        except ValueError:
            pass
            
        # Operator check
        if self.compare_node_value(node.value, ["<", "<=", ">=", ">", "+", "-", "*", "/", "="]):
            
            #print("CHECK: ", node.value)
            
            # Check that all of the children of this node are integers
            for child in node.children:
                if not self.typecheck(child, symbol_tables):
                    return False        # A typecheck failed
            return True                 # All children typecheched successfully
    
        # Symbol table check
        var_properties = symbol_tables.lookup(node.value)
        if var_properties is not None:
            # Integer []
            if var_properties[0] == "int[]":
                if len(node.children)==0:
                    print("ERROR: se esperaba int y se recibio int[] variable", node.value, "en", symbol_tables.scopeName)
                    self.error_detected = True
            
                # 1 child (array with index)
                else:
                    # Raw number index
                    try: 
                        index = int(node.children[0].value)
                        if index >= int(var_properties[1]["size"]):
                            print("ERROR: indice", index, "fuera de rango en la variable", node.value,"en", symbol_tables.scopeName)
                            self.error_detected = True
                            
                    # Check that variable inside is an int
                    except ValueError:
                        
                        return self.typecheck(node.children[0], symbol_tables)
                        #print(node)
                        #pass
                    #print(var_properties[0]["size"])
            
                # Int
                #elif var_properties[0] = "int":
                #print(node)
                #print(var_properties)
            
        

            
        # None of the options listed above worked
        return False
    
    
    # 
    
        
    # Helper function to check if value of the node is equal to at least one element in the array
    def compare_node_value(self, node_value, values_array):
        for value in values_array:
            if node_value == value:
                return True
        return False
