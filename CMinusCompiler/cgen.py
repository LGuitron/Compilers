from RuntimeErrors import *
from codeGeneration import *
from copy import deepcopy

# Global variable used for current sp_offset
sp_offset = 0

def codeGen(AST, filename):
    var_dict = {}
    
    f= open(filename,"w+")
    f.write(".data\nnewline0: .align 4 \n.asciiz \"\\n\" \n")
    f.write("negindex0: .align 4 \n.asciiz \"Error de runtime: No se permiten indices negativos\" \n")
    f.write("outbounds0: .align 4 \n.asciiz \"Error de runtime: Indice fuera de rango\" \n")
    declare_global_variables(AST, f, var_dict)
    f.write(".text\n.globl main\n\n")
    
    # START IN MAIN FUNCTION AFTER DECLARING GLOBALS
    f.write("j main\n")                 
    
    traverseCGEN(AST, f, var_dict)
    add_runtime_errors(f)
    
# Traverse tree and generate code on particular cases
# PARAMETERS
# node      : Current node checked
# f         : File pointer to write generated code
# var_dict  : Var_dictionary for storing variable names for the current scope with their corresponding sp_offset

# FUNCTION FOR IDENTIFYING GLOBAL VARIABLES
def declare_global_variables(node, f, var_dict):
    
    global global_arrays
    
    for child in node.children:

        # GLOBAL VARIABLE DECLARATIONS
        if child.value == "int": 
            
            # INT
            if len(child.children) == 1:
                f.write(child.children[0].value+ ": .word 0\n")
    
            # INT[SIZE] with .space
            elif len(child.children) == 2:
                arr_size = int(child.children[1].value)
                
                # MAKE LAST GLOBAL DECLARATION RESERVE SPACE
                f.write(".space " + str(4*arr_size) + "\n")
                f.write(child.children[0].value+ ": .word 0\n")
                global_arrays[child.children[0].value] = arr_size
                #global_arrays.append(child.children[0].value)

# FUNCTION FOR IDENTIFYING FUNCTION DECLARATIONS IN THE GLOBAL SCOPE
def traverseCGEN(node, f, var_dict):    
    
    global sp_offset
    
    # ONLY TRAVERSE NODES INSIDE FUNCTIONS
    for child in node.children:
        if child.value == "fun_declaration":
            
            function_name = child.children[1].value
            f.write("\n"+ function_name + ":\n\n")
            
            # MAIN FUNCTION
            if function_name == "main":
                traverse_function_nodes(child.children[3], f, var_dict)
                
            # OTHER FUNCTIONS
            else:
                
                # Add code for returning from function call
                f.write("move $fp $sp\n")
                f.write("sw $ra 0($sp)\n")
                f.write("addiu $sp $sp -4\n")
                
                # ADD PARAMETERS TO THE LOCAL DICTIONARY
                local_dict  = deepcopy(var_dict)
                params_node = child.children[2]
                
                #for i in range(len(params_node.children) -1, -1, -1):
                for i in range(len(params_node.children)):
                    current_param = params_node.children[i]
                    
                    # INT[]
                    if current_param.value == "int[]":                        
                        local_dict[current_param.children[0].value] = (sp_offset, -1)
                    else:
                        local_dict[current_param.children[0].value] = sp_offset
                    sp_offset += 4
                sp_offset += 4
                
                
                # ITERATE OVER COMPOUND STATEMENT ONLY
                traverse_function_nodes(child.children[3], f, local_dict)
                local_declarations = count_local_declarations(child.children[3])
                
                #local
                
                
                sp_offset -= 8 
                sp_offset -= local_declarations*4
                sp_offset -= len(params_node.children)*4
                
                #print(declaration_count)
                
                # RETURN TO CALLER
                f.write("addiu $sp $sp " + str(4*local_declarations)+ "\n")      # POP STACK FOR LOCAL DECLARATIONS
                f.write("lw $ra 4($sp)\n")
                f.write("addiu $sp $sp " + str(8 + 4*len(params_node.children))+ "\n")
                f.write("lw $fp 0($sp)\n")
                f.write("jr $ra\n")
                

# FUNCTION FOR TRAVERSING ALL NODES INSIDE A FUNCTION    
def traverse_function_nodes(node, f, var_dict):

    global sp_offset
    
    # INT DECLARATIONS
    if node.value == "int": 
            
        # INT
        if len(node.children) == 1:
            declare_int(node, f, var_dict, sp_offset)
            sp_offset += 4
    
        # INT[SIZE]
        elif len(node.children) == 2:
            declare_int_array(node, f, var_dict, sp_offset)
            arr_size = int(node.children[1].value)
            sp_offset += 4 * arr_size

    # ASSIGNMENTS
    elif node.value == "=": 
        assign_int(node, f, var_dict, sp_offset)
        

    # RESERVED OUTPUT FUNCTION
    elif node.value == "output" and len(node.children) == 1 and node.children[0].value == "_args":
        output_function(node, f, var_dict, sp_offset)

    # CUSTOM FUNCTION CALL
    elif len(node.children) == 1 and node.children[0].value == "_args":
        eval_node(node, f, var_dict, sp_offset)
    
    
    # RETURN VALUE
    elif node.value == "return":
        eval_node(node.children[0], f, var_dict, sp_offset)
    
    # RECURSIVE TREE TRAVERSAL
    else:
        for child in node.children:
            traverse_function_nodes(child, f, var_dict)
            
# HELPER FUNCTION FOR COUNTING LOCAL DECLARATIONS IN A GIVEN FUNCTION (FOR STACK POPPING)
def count_local_declarations(node):
    
    new_args = 0
    
    # INT DECLARATIONS
    if node.value == "int": 
            
        # INT
        if len(node.children) == 1:
            new_args += 1
    
        # INT[SIZE]
        elif len(node.children) == 2:
            arr_size = int(node.children[1].value)
            new_args += arr_size
            
    for child in node.children:
        new_args += count_local_declarations(child)
    return new_args
