from SymbolTable import SymbolTable 
from copy import deepcopy

def tabla(tree, imprime = True):
    
    globalTable = SymbolTable()                    # Start by initializing global symbol table
    
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
            globalTable.insert(name, _type, property_dict)
    
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
            currentScope = SymbolTable(globalTable)

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
                    currentScope.insert(p_name, p_type, {})
                    
                property_dict["params"] = global_param_list
                
             # TODO check declarations inside the function
            
            
            globalTable.addChild(currentScope)
            globalTable.insert(name, _type, property_dict)
                
    return globalTable

def semantica(tree, imprime = True):

    symbol_tables = tabla(tree, imprime)
    if imprime:
        print(symbol_tables)
    return symbol_tables
