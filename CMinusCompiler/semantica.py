from SymbolTable import SymbolTable 
from copy import deepcopy
from TypeChecks import *

'''
SYMBOL TABLE FUNCTION
'''
def tabla(tree, imprime = True):

    globalTable   = SymbolTable()                    # Start by initializing global symbol table
    register_variables(tree, globalTable)            # Register global variables in global symbol table
    next_node_st(tree, globalTable)                  # Function for building symbol tables recursively
    return globalTable, False                        # TODO determine if an error occured

# Helper function for traversing for building symbol tables
def next_node_st(node, current_symbol_table):
    
    #######################
    #FUNCTION DECLARATION #
    #######################
    if node.value == "fun_declaration":
        
        fun_type = node.children[0].value
        fun_name = node.children[1].value
        fun_properties = {}
        
        if node.children[2].value == "void":
            fun_properties["params"] = "void"
        else:
            parameters = []
            for child in node.children[2].children:
                parameters.append(child.value)
            fun_properties["params"] = parameters
        new_symbol_table = SymbolTable(current_symbol_table, fun_name)
        
        # Register function in this scope and in the parent scope
        new_symbol_table.insert(fun_name, fun_type, fun_properties)
        current_symbol_table.insert(fun_name, fun_type, fun_properties)
        
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
        new_symbol_table = SymbolTable(current_symbol_table, node.value)
        register_variables(node, new_symbol_table)
        current_symbol_table.addChild(new_symbol_table)
        
        for child in node.children:
            next_node_st(child, new_symbol_table)
    
    
    #####################################
    # TYPECHECK FOR ARITMETIC OPERATORS #
    #####################################
    elif compare_node_value(node.value, ["<", "<=", ">=", ">", "+", "-", "*", "/", "="]):
        typecheck(node, current_symbol_table)
        #print(node)
        #print("TC: ", node.value)
    
    
    ##################
    #GO TO NEXT NODE #
    ##################
    else:
        for child in node.children:
            next_node_st(child, current_symbol_table)


# Helper Function for registering variable declarations in a given symbol table
def register_variables(node, symbol_table):
    for child in node.children:
        
        if child.value == "int":

            # int
            if len(child.children)==1:
                symbol_table.insert(child.children[0].value, "int", {})
                
            # int[]
            else:
                property_dict         = {}
                property_dict["size"] = child.children[1].value
                symbol_table.insert(child.children[0].value, "int[]", property_dict)
        
        # Declarations always go first
        else:
            break

'''
MAIN SEMANTIC FUNCTION CALL
'''
def semantica(tree, imprime = True):

    symbol_tables, errorDetected = tabla(tree, imprime)
    
    # If there were no errors when building symbol table continue with typechecking
    #if not errorDetected:
    #    traversal = TraverseTree()
    #    errorDetected = traversal.traverse(tree, symbol_tables)
    
    if imprime and not errorDetected:
        #print(tree)
        print(symbol_tables)
    return symbol_tables
