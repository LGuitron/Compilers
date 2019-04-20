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

####################
# INT DECLARATIONS #
####################
def declare_int(node, f, var_dict, sp_offset):

    var_dict[node.children[0].value] = sp_offset

    # All integers are initialized with value of 0
    f.write("li $a0 0\n")
    f.write("sw $a0 0($sp)\n")
    f.write("addiu $sp $sp -4\n")
    

######################
# INT[] DECLARATIONS #
######################
def declare_int_array(node, f, var_dict, sp_offset):

    # Store sp_offset and array size in dictionary
    arr_size = int(node.children[1].value)
    var_dict[node.children[0].value] = (sp_offset, arr_size)

    # All integers are initialized with value of 0
    for i in range(arr_size):
        f.write("li $a0 0\n")
        f.write("sw $a0 0($sp)\n")
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
        
        
        # IN CASE OF ARRAY GET POSITION IN $a2 REGISTER AND SAVE IN THAT LOCATION
        if len(child.children) == 1:
            
            f.write("move $a1 $a0\n")                            # COPY NODE VALUE'S VALUE TO $a1 REGISTER BEFORE EVALUATING INDEX
            eval_int_array(child, f, var_dict, sp_offset)
            f.write("sw $a1 0($a2)"+"\n")
        
        # STORE INDEX IN ITS CURRENT SP VALUE
        else:
            current_sp = var_dict[child.value]
            f.write("sw $a0 " +str(sp_offset - current_sp)+"($sp)"+"\n")

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
            #eval_arithmetic(node, f, var_dict, sp_offset)
            eval_arithmetic(node, f, var_dict, 0)
        
        # LOOK FOR VARIABLE SP_OFFSET VALUE IN DICTIONARY
        else:
            
            
            # TODO CHECK CASE FOR FUNCTION EVALUATION
            
            # INT [index]
            if (len(node.children) == 1):                
                eval_int_array(node, f, var_dict, sp_offset)
                f.write("lw $a0 ($a2)\n")
            
            # INT
            else:
                current_sp = var_dict[node.value]
                f.write("lw $a0 " +str(sp_offset - current_sp)+"($sp)" + "\n")
            


#################################################
# EVALUATE INT[INDEX] (RETURNS POSITION IN $a2) #
#################################################
def eval_int_array(node, f, var_dict, sp_offset):

    current_sp = var_dict[node.value]
    arr_size   = current_sp[1]
    current_sp = current_sp[0] 
    
    # EVALUATE INDEX OF ARRAY
    eval_node(node.children[0], f, var_dict, sp_offset)
    
    # CHECK THAT INDEX IS IN BOUNDS
    f.write("blt $a0 $zero Negindexerror\n")                         # NEGATIVE INDEX ERROR
    f.write("li $a2 " + str(arr_size) + "\n")                        # LOAD ARRAY SIZE INTO $a2 REGISTER
    f.write("bge $a0 $a2 Outboundserror\n")                          # OUT OF BOUNDS ERROR
    
    # INDEX IS OK
    f.write("move $a2 $sp\n")                                        # STORE CURRENT STACK POINTER IN $a2
    f.write("addiu $a2 $a2 " + str(sp_offset - current_sp) + "\n")   # ADD SP_OFFSET OF ARRAY START TO $a2 REGISTER
    f.write("li $a3 4\n")                                            # LOAD CONSTANT 4 IN REGISTER
    f.write("mul $a0 $a0 $a3\n")                                     # MULTPLY INDEX VALUE BY 4
    f.write("sub $a2 $a2 $a0\n")                                     # SUBSTRACT THIS VALUE TO $a2 to get to the right position
    

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
                eval_arithmetic(child, f, var_dict, sp_offset - 4 * (i+1))
                operands.append(sp_offset - 4 * (i+1))
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
