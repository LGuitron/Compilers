from SymbolTable import SymbolTable 
from copy import deepcopy
from TypeChecks import *

errorDetected = False
last_function = ""

# Reserve node names (they will not be looked in the symbol table)
nodeNames = ["int", "void", "declaration_list", "fun_declaration", "_params", "int[]", "compound_statement", "if", "while", "return", "_args"]

'''
SYMBOL TABLE FUNCTION
'''
def tabla(tree, imprime = True):

    error = False
    globalTable   = SymbolTable()                             # Start by initializing global symbol table
    globalTable.insert("input", "int", {"params":"void"})     # Register special input() function
    globalTable.insert("output", "void", {"params":["int"]})  # Register special output() function
    error = error or register_variables(tree, globalTable)    # Register global variables in global symbol table
    next_node_st(tree, globalTable)                           # Function for building symbol tables recursively
    error = error or checkReturns(globalTable)                # Check for errors in return statements  

    # Check that last function is main
    if last_function != "main":
        print("Error: la ultima funcion declarada en el programa debe llamarse main")
        return globalTable, True
    return globalTable, (error or errorDetected)

# Helper function for traversing for building symbol tables
def next_node_st(node, current_symbol_table):
    
    global errorDetected
    global last_function

    #######################
    #FUNCTION DECLARATION #
    #######################
    if node.value == "fun_declaration":
        
        
        fun_type = node.children[0].value
        fun_name = node.children[1].value
        fun_properties = {}
        
        # If int is returned require return int; validation
        if fun_type == "int":
            new_symbol_table = SymbolTable(current_symbol_table, True, fun_name, fun_type)
        else:
            new_symbol_table = SymbolTable(current_symbol_table, False, fun_name, fun_type)
        
        if node.children[2].value == "void":
            fun_properties["params"] = "void"
        else:
            parameters = []
            for child in node.children[2].children:
                parameters.append(child.value)
            fun_properties["params"] = parameters
            register_variables(node.children[2], new_symbol_table)
        
        
        # Register function in this scope and in the parent scope
        error = False
        error = new_symbol_table.insert(fun_name, fun_type, fun_properties)
        error = current_symbol_table.insert(fun_name, fun_type, fun_properties)
        
        if error:
            errorDetected = True
        
        last_function = fun_name
        
        # Register compund statement variables
        for child in node.children:            
            # Compound statement function declarations
            if child.value == "compound_statement":
                register_variables(child, new_symbol_table)
                
                for gradnchild in child.children:
                    next_node_st(gradnchild, new_symbol_table)
        current_symbol_table.addChild(new_symbol_table)

    #######################################
    #INNER COMPOUND STATEMENT DECLARATION #
    #######################################
    elif node.value == "compound_statement":
        new_symbol_table = SymbolTable(current_symbol_table, False, node.value, current_symbol_table.returnType)
        register_variables(node, new_symbol_table)
        current_symbol_table.addChild(new_symbol_table)
        
        for child in node.children:
            next_node_st(child, new_symbol_table)
    
    
    #####################################
    # TYPECHECK FOR ARITMETIC OPERATORS #
    #####################################
    elif compare_node_value(node.value, ["<", "<=", "==", "!=", ">=", ">",  "+", "-", "*", "/", "="]):
        success = typecheck(node, current_symbol_table)
        errorDetected = errorDetected or (not success)        
        
    
    ##########################
    # PREVENT VOID VARIABLES #
    ##########################
    elif node.value == "void" and len(node.children) > 0:
        print("Error: no se pueden declarar variables de tipo void (variable", node.children[0].value, ") en", current_symbol_table.scopeName)
        errorDetected = True
        
    ###############################
    # CHECK FUNCTION RETURN VALUE #
    ###############################
    elif node.value == "return":
        
        # Int return
        if current_symbol_table.returnType == "int":
            
            # Retorno exitoso de int
            if len(node.children) == 1 and typecheck(node.children[0], current_symbol_table):
                current_symbol_table.returnVerified = True
            
            else:
                print("Error: se esperaba retorno de int en", current_symbol_table.scopeName)
                errorDetected = True
                
        # Void return
        elif current_symbol_table.returnType == "void":
            print("Error: la funcion",current_symbol_table.scopeName, "es void y se declaro con un return")
            errorDetected = True
    
    ##########################
    # CHECK IDENTIFIER NODES #
    ##########################
    elif node.value not in nodeNames:

        # Check for raw numbers
        try: 
            int(node.value)
        
        # Look at symbol table
        except ValueError:

            var_properties = current_symbol_table.lookup(node.value)
            if var_properties is None:
                print("Error:", node.value, "no fue declarada en", current_symbol_table.scopeName)
                errorDetected = True

            # Check that the Identifier is used properly Variable, Function or Array
            else:
                dict_length = 0
                for k, v in var_properties[1].items():
                    dict_length += 1
                
                # IS INTEGER
                if var_properties[0] == "int":
                
                    # INT VARIABLE
                    if dict_length == 0:
                        if len(node.children) > 0:
                            print("Error:", node.value, "es una variable y no puede ser llamada como arreglo o funcion")
                            errorDetected = True
                        
                    # TODO INT FUNCTION
                    else:
                        success = validate_parameters(node, var_properties, current_symbol_table)
                        if not success:
                            errorDetected = True
                        #print("ID: " , node)
                        #print(var_properties)
                
                
                # INT ARRAY
                elif var_properties[0] == "int[]":
                    if len(node.children)>0 and node.children[0].value == "_args":
                        print("Error:", node.value, "es un arreglo y no puede ser llamado como funcion")
                        errorDetected = True
                
                # VOID FUNCTION
                else:
                    
                    if len(node.children) == 0:
                        print("Error:", node.value, "es una funcion y no puede ser llamada como variable")
                        errorDetected = True
                    
                    elif node.children[0].value != "_args":
                        print("Error:", node.value, "es una funcion y no puede ser llamada como arreglo")
                        errorDetected = True
                    
                    else:
                        success = validate_parameters(node, var_properties, current_symbol_table)
                        if not success:
                            errorDetected = True

    #######################################
    # CHECK IF/WHILE CONDITIONS TO BE INT #
    #######################################
    elif node.value == "if" or node.value == "while":
        success = typecheck(node.children[0], current_symbol_table)
        errorDetected = errorDetected or (not success)      
    
        for child in node.children:
            next_node_st(child, current_symbol_table)
        
        
    ##################
    #GO TO NEXT NODE #
    ##################
    else:
        for child in node.children:
            next_node_st(child, current_symbol_table)


# Helper Function for registering variable declarations in a given symbol table
def register_variables(node, symbol_table):
    
    errorDetected = False
    
    for child in node.children:
        
        new_error = False
        
        # Int or Int[] with set size
        if child.value == "int":

            # int
            if len(child.children)==1:
                new_error = symbol_table.insert(child.children[0].value, "int", {})
                
            # int[]
            else:
                property_dict         = {}
                property_dict["size"] = child.children[1].value
                new_error = symbol_table.insert(child.children[0].value, "int[]", property_dict)
        
        # Int[] without set value
        elif child.value == "int[]":
            new_error = symbol_table.insert(child.children[0].value, "int[]", {})

        errorDetected = errorDetected or new_error
    return errorDetected

# Helper function to determine if there are Errors in the return values of a scope
# Return if an error was detected
def checkReturns(current_symbol_table):
    
    error = False
    if current_symbol_table.reqReturnVerification and not current_symbol_table.returnVerified:
        print("Error: se esperaba retorno de int en", current_symbol_table.scopeName)
        error = True

    for child in current_symbol_table.childTables:
        new_error = checkReturns(child)
        error     = error or new_error
    return error

'''
MAIN SEMANTIC FUNCTION CALL
'''
def semantica(tree, imprime = True):
    symbol_tables, errorDetected = tabla(tree, imprime)
    if imprime and not errorDetected:
        print(symbol_tables)
    
    # Terminate execution if there was an error
    else:
        exit()
    return symbol_tables
