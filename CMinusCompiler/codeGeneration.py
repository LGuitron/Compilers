from TypeChecks import compare_node_value

######################################
# ARITHMETIC INSTRUCTIONS DICTIONARY #
######################################
arithmetic_dict = {
                    "+" : "add",
                    "-" : "sub",
                    "*" : "mul",
                    "/" : "div",
                    "<" : "slt",
                    "<=": "sle",
                    "==": "seq",
                    "!=": "sne",
                    ">=": "sge",
                    ">" : "sgt"
                  }

#########################
# VARIABLE DECLARATIONS #
#########################
def declare_int(node, f, var_dict, sp_offset):

    var_dict[node.children[0].value] = sp_offset 

    # All integers are initialized with value of 0
    f.write("li $a0 0\n")
    f.write("sw $a0 " +str(sp_offset)+"($sp)"+"\n")
    f.write("addiu $sp $sp -4\n")
    
########################
# VARIABLE ASSIGNMENTS #
########################
def assign_int(node, f, var_dict, sp_offset):
    
    # The assigned value is going to be the last child of the = node
    value_node = node.children[len(node.children)-1]
    eval_node(value_node, f, var_dict, sp_offset)

    for i in range(len(node.children)-1):
        child = node.children[i]
        current_sp = var_dict[child.value]
        f.write("sw $a0 " +str(current_sp)+"($sp)"+"\n")
    
    # TODO ASSIGNMENT FOR ARRAYS


###################
# OUTPUT FUNCTION #
###################
def output_function(node, f, var_dict, sp_offset):
    
    f.write("li $v0 1\n")
    value_node = node.children[0].children[0]
    eval_node(value_node, f, var_dict, sp_offset)
    f.write("syscall\n")
    
    # Print line break
    f.write("li $v0 4\n")
    f.write("la $a0 newline\n")
    f.write("syscall\n")
    
    # TODO PRINT ARRAY AT INDEX
    

################################
# FUNCTION FOR NODE EVALUATION #
################################
def eval_node(node, f, var_dict, sp_offset):
    
    # RAW NUMBERS
    try: 
        value = int(node.value)
        f.write("li $a0 " + str(value) + "\n")

    except ValueError:
        
        # ARITHMETIC OPERATORS
        if compare_node_value(node.value, ["<", "<=", "==", "!=", ">=", ">",  "+", "-", "*", "/"]):
            eval_arithmetic(node, f, var_dict, sp_offset)
        
        # LOOK FOR VARIABLE SP_OFFSET VALUE IN DICTIONARY
        else:
            current_sp = var_dict[node.value]
            f.write("lw $a0 " +str(current_sp)+"($sp)" + "\n")


###################################
# EVALUATE ARITHMETIC EXPRESSIONS #
###################################
def eval_arithmetic(node, f, var_dict, sp_offset):
    
    operands     = []
    
    # List to determine how was the operand evaluated
    # True - int literal
    # False - Variable / Intermediate result in RAM
    eval_method = []   
    
    #for child in node.children:
    for i in range(len(node.children)):    
        child = node.children[i]
        value = child.value
        
        try: 
            value = int(value)
            operands.append(value)
            eval_method.append(True)
            
        except ValueError:
            
            # RECURSIVE ARITHMETIC EXPRESSION
            if compare_node_value(value, ["<", "<=", "==", "!=", ">=", ">",  "+", "-", "*", "/"]):
                eval_arithmetic(child, f, var_dict, sp_offset + 4)
                operands.append(sp_offset + 4)
                eval_method.append(False)
            
            # LOOK FOR SP_OFFSET
            else:
                value = var_dict[value]
                operands.append(value)
                eval_method.append(False)
    

    
    # Load operands in temporal registries $t0 and $t1
    for i in range(len(node.children)):
        child = node.children[i]
        # Integer literal
        if eval_method[i]:         
            f.write("li $a" + str(i) + " " + str(operands[i]) + "\n")
        
        # Variable or intermediate expression stored in RAM        
        else:                           # Variable /
            f.write("lw $a" + str(i) + " " + str(operands[i]) +"($sp)\n")

    f.write(arithmetic_dict[node.value]+ " $a0 $a0 $a1\n")
    f.write("sw $a0 " + str(sp_offset) + "($sp)\n")         # Store in main memory
