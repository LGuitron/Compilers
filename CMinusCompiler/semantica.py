from TraverseTree import TraverseTree
from SymbolTable import SymbolTable 
from copy import deepcopy

'''
SYMBOL TABLE FUNCTION
'''
def tabla(tree, imprime = True):
    
    globalTable   = SymbolTable()                    # Start by initializing global symbol table
    errorDetected = False                            # Boolean to determine if redeclaration errors occured
    
    # Go through all of the children of the root node (either global variable declaration or function declaration)
    for i in range (len(tree.children)):
        
        current_node  = tree.children[i]
        property_dict = {}

        '''
        GLOBAL VARIABLE
        '''
        # Addentry to the symbol table when finding either a void or int declaration
        if current_node.value == "int":
            name            = current_node.children[0].value
            _type           = "int"
            propery_dict    = deepcopy(property_dict)
            property_dict   = {}
            
            # Check for int array
            if len(current_node.children) > 1:
                _type = "int[]"
                property_dict["size"] = current_node.children[1].value

            # Add entry to the table
            error = globalTable.insert(name, _type, property_dict)
            if error:
                errorDetected = True
    
        '''
        FUNCTION
        '''

        # Create local symbol table when detecting a function
        if current_node.value == "fun_declaration":            
            _type             = current_node.children[0].value
            name              = current_node.children[1].value
            propery_dict      = deepcopy(property_dict)
            property_dict     = {}
            
            # Local symbol table declaration
            currentScope = SymbolTable(globalTable, name)
            
            
            '''
            FUNCTION PARAMETERS
            '''
            
            params_node = current_node.children[2]
            if params_node.value == "void":
                property_dict["params"] = "void"

            # Iterate through parameters for adding in both symbol tables (global and local)
            else:
                global_param_list = []
                for j in range(len(params_node.children)):
                    local_node = params_node.children[j]
                    p_type = local_node.value
                    p_name = local_node.children[0].value
                    global_param_list.append(p_type)
                    error = currentScope.insert(p_name, p_type, {})
                    if error:
                        errorDetected = True
                    
                property_dict["params"] = global_param_list
            
            # Add function declaration to the global scope
            error = globalTable.insert(name, _type, property_dict)
            error = currentScope.insert(name, _type, property_dict)
            if error:
                errorDetected = True
            
            
            # Add variable declarations made inside the function
            '''
            FUNCTION VARIABLES
            '''
            function_child = 3
            while current_node.children[function_child].value == "int":
                local_int = current_node.children[function_child]
                # Check if the declaration is an int or an int[]
                # Int
                p_name = local_int.children[0].value
                if len(local_int.children) == 1:
                    error = currentScope.insert(p_name, "int", {})
                    if error:
                        errorDetected = True
                    
                # Int[]
                else:
                    propery_dict          = deepcopy(property_dict)
                    property_dict         = {}
                    property_dict["size"] = local_int.children[1].value
                    error = currentScope.insert(p_name, "int[]", property_dict)
                    if error:
                        errorDetected = True
                    
                function_child += 1
            
            globalTable.addChild(currentScope)
                
    return globalTable, errorDetected



'''
TYPE CHECK FUNCTION
'''
def semantica(tree, imprime = True):

    symbol_tables, errorDetected = tabla(tree, imprime)
    
    # If there were no errors when building symbol table continue with typechecking
    if not errorDetected:
        traversal = TraverseTree()
        errorDetected = traversal.traverse(tree, symbol_tables)
    
    if imprime and not errorDetected:
        #print(tree)
        print(symbol_tables)
    return symbol_tables
