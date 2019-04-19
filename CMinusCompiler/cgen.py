from codeGeneration import *

# Global variable used for current sp_offset
sp_offset = 0

def codeGen(AST, filename):
    f= open(filename,"w+")
    f.write(".data\nnewline: .asciiz \"\\n\" \n")
    f.write(".text\n.globl main\n\nmain:\n")
    
    # TODO declare and store global variables
    
    var_dict = {}
    traverseCGEN(AST, f, var_dict)
    
    
    f.write("\nend:\nli $v0 10\nsyscall")
    
    #for key, value in var_dict.items():
    #    print(key, " : " , value)
    
    
    
    
# Traverse tree and generate code on particular cases

# PARAMETERS
# node      : Current node checked
# f         : File pointer to write generated code
# var_dict  : Var_dictionary for storing variable names for the current scope with their corresponding sp_offset

def traverseCGEN(node, f, var_dict):
    
    global sp_offset
    
    
    # INT DECLARATIONS
    if node.value == "int": 
        
        # Function
        if len(node.children) == 0:
            print("F: " , node)
            
        # Variable
        elif len(node.children) == 1:
            declare_int(node, f, var_dict, sp_offset)
            sp_offset += 4
    
        # Arrays
        else:
            print("A: " , node)


    # ASSIGNMENTS
    elif node.value == "=": 
       assign_int(node, f, var_dict, sp_offset)
        

    # RESERVED OUTPUT FUNCTION
    elif node.value == "output" and len(node.children) == 1 and node.children[0].value == "_args":
        output_function(node, f, var_dict, sp_offset)
    

    for child in node.children:
        traverseCGEN(child, f, var_dict)
        
    
        
        
