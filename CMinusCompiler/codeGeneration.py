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
    value = node.children[len(node.children)-1].value

    # RAW NUMBERS
    try: 
        value = int(value)
        f.write("li $a0 " + str(value) + "\n")
    
    
    except ValueError:
        
        # ARITHMETIC OPERATORS
        if value == "+":
            eval_arithmetic(node.children[len(node.children)-1], f, var_dict)
            #print(value)
        
        # LOOK FOR VARIABLE SP_OFFSET VALUE IN DICTIONARY
        else:
            current_sp = var_dict[value]
            f.write("lw $a0 " +str(current_sp)+"($sp)" + "\n")
    
    
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
    
    # RAW NUMBERS
    try: 
        value = int(node.children[0].children[0].value)
        f.write("li $a0 "+ str(value)+ "\n")
    
    
    # LOOK FOR VARIABLE SP_OFFSET VALUE
    except ValueError:
        current_sp = var_dict[node.children[0].children[0].value]
        f.write("lw $a0 " +str(current_sp)+"($sp)\n")
    f.write("syscall\n")
    
    # Print line break
    f.write("li $v0 4\n")
    f.write("la $a0 newline\n")
    f.write("syscall\n")
    
    # TODO PRINT ARRAY AT INDEX
    
    
###################################
# EVALUATE ARITHMETIC EXPRESSIONS #
###################################
def eval_arithmetic(node, f, var_dict, write_register="0"):
    
    operands     = []
    
    # List to determine how was the operand evaluated
    # 0 - int literal
    # 1 - Recursive Arithmetic
    # 2 - Looked for variable
    eval_method = []   
    
    #for child in node.children:
    for i in range(len(node.children)):    
        child = node.children[i]
        value = child.value
        
        try: 
            value = int(value)
            operands.append(value)
            eval_method.append(0)
            
        except ValueError:
            
            # RECURSIVE ARITHMETIC EXPRESSION
            if value == "+":
                eval_arithmetic(child, f, var_dict, i)
                operands.append(0)
                eval_method.append(1)
            
            # LOOK FOR SP_OFFSET
            else:
                value = var_dict[value]
                operands.append(value)

                eval_method.append(2)
                
    
    # Load operands in temporal registries $t0 and $t1
    for i in range(len(node.children)):
        if eval_method[i] == 0:         # Literal
            f.write("li $a" + str(i) + " " + str(operands[i]) + "\n")
        #elif eval_method[i] == 1:       # Recursive arithmetic
            
        
        else:                           # Variable
            f.write("lw $a" + str(i) + " " + str(operands[i]) +"($sp)\n")
            
        # TODO check for more arithmetic operations
        f.write("add $a" +str(write_register) + " $a0 $a1\n")
