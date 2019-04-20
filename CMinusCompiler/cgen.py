from RuntimeErrors import *
from codeGeneration import *

# Global variable used for current sp_offset
sp_offset = 0

def codeGen(AST, filename):
    var_dict = {}
    
    f= open(filename,"w+")
    f.write(".data\nnewline: .asciiz \"\\n\" \n")
    f.write("negindex: .asciiz \"Error de runtime: No se permiten indices negativos\" \n")
    f.write("outbounds: .asciiz \"Error de runtime: Indice fuera de rango\" \n")
    f.write(".text\n.globl main\n\n")
    declare_global_variables(AST, f, var_dict)
    
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
    global sp_offset
    for child in node.children:

        # GLOBAL VARIABLE DECLARATIONS
        if child.value == "int": 
            
            # INT
            if len(child.children) == 1:
                declare_int(child, f, var_dict, sp_offset)
                sp_offset += 4
        
            # INT[SIZE]
            elif len(child.children) == 2:
                declare_int_array(child, f, var_dict, sp_offset)
                arr_size = int(child.children[1].value)
                sp_offset += 4 * arr_size


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
                for grandchild in child.children:
                    traverse_function_nodes(grandchild, f, var_dict)
                
            # OTHER FUNCTIONS
            else:
                # Add code for returning from function call
                f.write("move $fp $sp\n")
                f.write("sw $ra 0($sp)\n")
                f.write("addiu $sp $sp -4\n")
                
                # TODO add param count to sp_offset as well
                
                sp_offset += 8
            
                for grandchild in child.children:
                    traverse_function_nodes(grandchild, f, var_dict)
                sp_offset -= 8
                
                # POP THIS FUNCTION'S STACK
                declaration_count = count_local_declarations(child)
                sp_offset -= declaration_count*4
                
                # RETURN TO CALLER
                f.write("addiu $sp $sp " + str(declaration_count*4) + "\n")
                f.write("lw $ra " + str(4 + 4*0) + "($sp)\n")
                f.write("addiu $sp $sp " + str(8 + 4*0)+ "\n")        # TODO FIX THIS VALUE DEPENDING ON PARAMS SIZE
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
    
