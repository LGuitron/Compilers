from TypeChecks import compare_node_value

global_arrays = {}                    # Dictionary containing global arrays with their corresponding sizes



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

    # COPY NODE VALUE'S VALUE TO $t0 REGISTER BEFORE EVALUATING THE REMAINING CHILDREN
    f.write("move $t0 $a0\n")
    for i in range(len(node.children)-1):
        child = node.children[i]
        
        # LOCAL VARIABLE ASSIGNMENT
        if child.value in var_dict:
        
            # IN CASE OF ARRAY GET POSITION IN $t0 REGISTER AND SAVE IN THAT LOCATION
            if len(child.children) == 1:
                eval_int_array(child, f, var_dict, sp_offset)
                f.write("sw $t0 0($a2)"+"\n")
            
            # STORE INDEX IN ITS CURRENT SP VALUE
            else:
                current_sp = var_dict[child.value]
                f.write("sw $t0 " +str(sp_offset - current_sp)+"($sp)"+"\n")
                
        # GLOBAL VARIABLE ASSIGNMENT
        else:
            
            #INT[]
            if len(child.children) == 1:
                eval_node(child.children[0], f, var_dict, sp_offset)        # NODE INDEX IN $a0 register
                f.write("li $a1 4\n")
                f.write("mul $a0 $a0 $a1\n")                                # MULTPLY INDEX BY 4
                f.write("la $a1 " + child.value + "\n")                     # LOAD ADDRESS OF START OF ARRAY
                f.write("sub $a1 $a1 $a0\n")                                # GET TO THIS ARRAY POSITION
                f.write("sw $t0 0($a1)\n")

            #INT
            else:
                f.write("la $a0 " + child.value + "\n")
                f.write("sw $t0 0($a0)\n")


##################
# INPUT FUNCTION #
##################
def input_function(f):

    # Print input message
    f.write("li $v0 4\n")
    f.write("la $a0 input0\n")
    f.write("syscall\n")   
    
    # Read Input
    f.write("li $v0 5\n")
    f.write("syscall\n")
    
    # Store value in $a0
    f.write("move $a0 $v0\n")
    
    # Print line break
    #f.write("li $v0 4\n")
    #f.write("la $a0 newline0\n")
    #f.write("syscall\n")    


###################
# OUTPUT FUNCTION #
###################
def output_function(node, f, var_dict, sp_offset):

    value_node = node.children[0].children[0]
    eval_node(value_node, f, var_dict, sp_offset)
    f.write("li $v0 1\n")
    f.write("syscall\n")
    
    # Print line break
    f.write("li $v0 4\n")
    f.write("la $a0 newline0\n")
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
            eval_arithmetic(node, f, var_dict, 0, sp_offset)
            
        # LOOK FOR VARIABLE SP_OFFSET VALUE IN DICTIONARY
        else:
            
            # LOCAL VARIABLE (LOOK IN STACK)
            if node.value in var_dict:
            
                # INT [index]
                if len(node.children) == 1:
                    eval_int_array(node, f, var_dict, sp_offset)
                    f.write("lw $a0 0($a2)\n")
                
                # INT OR INT[] (without index as it was passed as parameter)
                else:
                    current_sp = var_dict[node.value]
                    
                    # INT
                    if type(current_sp) is int:
                        f.write("lw $a0 " +str(sp_offset - current_sp)+"($sp)" + "\n")
                        
                    # INT[]
                    else:
                        f.write("lw $a0 " +str(sp_offset - current_sp[0])+"($sp)" + "\n")
                    
            # FUNCTION CALL
            elif len(node.children) > 0 and node.children[0].value == "_args":
                
                
                # RESERVED INPUT FUNCTION
                if node.value == "input" and node.children[0].children[0].value == "void":
                    input_function(f)
                
                # REGULAR FUNCTION
                else:
                    # STORE CALLER FP
                    f.write("sw $fp 0($sp)\n")
                    f.write("addiu $sp $sp -4\n")
                    sp_offset += 4


                    for i in range(len(node.children[0].children)):
                        param = node.children[0].children[i]  
                        
                        if param.value != "void":
                            
                            # RAW INT
                            try: 
                                value = int(param.value)
                                eval_node(param, f, var_dict, sp_offset + 4*i)
                                
                            except ValueError:

                                # GLOBAL VARIABLE
                                if param.value not in var_dict:
                                    
                                    
                                    # EVALUATE ARITHMETIC EXPRESSIONS
                                    if compare_node_value(param.value, ["<", "<=", "==", "!=", ">=", ">",  "+", "-", "*", "/"]):
                                        eval_node(param, f, var_dict, sp_offset + 4*i)
                                    
                                    # GLOBAL INT[]
                                    elif param.value in global_arrays:
                                        f.write("la $a0 " + param.value + "\n")          # ADDRESS OF GLOBAL ARRAY START IN $A1 registe
                                    
                                    # GLOBAL INT
                                    else:
                                        f.write("la $a0 " + param.value + "\n")
                                        f.write("lw $a0 0($a0)\n")
                                
                                # LOCAL INT VARIABLE
                                elif type(var_dict[param.value]) is int:
                                    eval_node(param, f, var_dict, sp_offset + 4*i)

                                # LOCAL INT[] VARIABLE
                                else:
                                    current_sp = var_dict[param.value][0]
                                    current_sp = (sp_offset + 4*i) - current_sp
                                    
                                    # CHECK IF IS SECOND TIME PASSED AS PARAMETER
                                    if var_dict[param.value][1] == -1:
                                        f.write("move $a1 $sp\n")                        # STORE CURRENT SP OFFSET IN $A1 register
                                        f.write("addiu $a1 " + str(current_sp) + "\n")   # GET ADDRESS OF OFFSET TO TRUE ARRAY
                                        f.write("lw $a0 0($a1)\n")                       # LOAD TRUE OFFSET FROM $A1 register

                                    else:
                                        f.write("move $a0 $sp\n")                        # STORE CURRENT SP OFFSET IN $A0 register
                                        f.write("addiu $a0 " + str(current_sp) + "\n")   # GET ADDRESS OF ARRAY START IN $A0 register
                                    
                            f.write("sw $a0 0($sp)\n")
                            f.write("addiu $sp $sp -4\n")
                    
                    # JUMP TO FUNCTION    
                    f.write("jal " + node.value + "\n")

            # LOOK FOR GLOBAL VARIABLE
            else:
                
                #INT[]
                if len(node.children) == 1:

                    arr_size = global_arrays[node.value]
                    eval_node(node.children[0], f, var_dict, sp_offset)        # NODE INDEX IN $a0 register
                    
                    # CHECK THAT INDEX IS IN BOUNDS
                    f.write("blt $a0 $zero Negindexerror\n")                   # NEGATIVE INDEX ERROR
                    f.write("li $a2 " + str(arr_size) + "\n")                  # LOAD ARRAY SIZE INTO $a2 REGISTER
                    f.write("bge $a0 $a2 Outboundserror\n")                    # OUT OF BOUNDS ERROR

                    # INDEX IS OK
                    f.write("li $a1 4\n")
                    f.write("mul $a0 $a0 $a1\n")                               # MULTPLY INDEX BY 4
                    f.write("la $a1 " + node.value + "\n")                     # LOAD ADDRESS OF START OF ARRAY
                    f.write("sub $a1 $a1 $a0\n")                               # GET TO THIS ARRAY POSITION
                    f.write("lw $a0 0($a1)\n")

                # INT
                else:
                    f.write("la $a0 " + node.value + "\n")
                    f.write("lw $a0 0($a0) \n")


#################################################
# EVALUATE INT[INDEX] (RETURNS POSITION IN $a2) #
#################################################
def eval_int_array(node, f, var_dict, sp_offset):

    current_sp = var_dict[node.value]
    arr_size   = current_sp[1]
    current_sp = current_sp[0] 
    
    # Array passed by reference to a function (value in sp_offset)
    # TODO CHECK THAT INDEX IS IN BOUNDS
    if arr_size == -1:
        
        # EVALUATE INDEX OF ARRAY
        eval_node(node.children[0], f, var_dict, sp_offset)
        
        f.write("move $a2 $sp\n")                                        # STORE CURRENT STACK POINTER IN $A2
        f.write("addiu $a2 $a2 " + str(sp_offset - current_sp) + "\n")   # GET ADDRESS OF ARRAY ADDRESS IN $A2
        f.write("lw $a2 0($a2)\n")                                       # LOAD ARRAY START ADDRESS IN $A2
        
        f.write("li $a3 4\n")                                            # LOAD CONSTANT 4 IN REGISTER
        f.write("mul $a0 $a0 $a3\n")                                     # MULTPLY INDEX VALUE BY 4
        f.write("sub $a2 $a2 $a0\n")                                     # SUBSTRACT THIS VALUE TO $a2 to get to the right position
        
        
    else:
        
        # EVALUATE INDEX OF ARRAY
        eval_node(node.children[0], f, var_dict, sp_offset)
        
        # CHECK THAT INDEX IS IN BOUNDS
        f.write("blt $a0 $zero Negindexerror\n")                         # NEGATIVE INDEX ERROR
        f.write("li $a2 " + str(arr_size) + "\n")                        # LOAD ARRAY SIZE INTO $a2 REGISTER
        f.write("bge $a0 $a2 Outboundserror\n")                          # OUT OF BOUNDS ERROR
        
        # INDEX IS OK
        f.write("move $a2 $sp\n")                                       # STORE CURRENT STACK POINTER IN $a2
        f.write("addiu $a2 $a2 " + str(sp_offset - current_sp) + "\n")  # ADD SP_OFFSET OF ARRAY START TO $a2 REGISTER
        f.write("li $a3 4\n")                                            # LOAD CONSTANT 4 IN REGISTER
        f.write("mul $a0 $a0 $a3\n")                                     # MULTPLY INDEX VALUE BY 4
        f.write("sub $a2 $a2 $a0\n")                                     # SUBSTRACT THIS VALUE TO $a2 to get to the right position

###################################
# EVALUATE ARITHMETIC EXPRESSIONS #
###################################

def eval_arithmetic(node, f, var_dict, sp_offset, abs_sp_offset):
    
    operands     = []
    
    # List to determine how was the operand evaluated
    # 0 - int literal
    # 1 - Variable or Intermediate result (+, -, ...)
    # 2 - int[]
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
            if compare_node_value(value, ["<", "<=", "==", "!=", ">=", ">",  "+", "-", "*", "/"]):
                eval_arithmetic(child, f, var_dict, sp_offset - 4 * (i+1), abs_sp_offset)
                operands.append(sp_offset - 4 * (i+1))
                eval_method.append(1)
            
            # LOOK FOR SP_OFFSET
            else:
                
                # INT[INDEX] OR FUNCTION
                if (len(child.children) == 1):
                    
                    # FUNCTION
                    if child.children[0].value == "_args":
                        eval_node(child, f, var_dict, abs_sp_offset)
                        f.write("sw $a0 " + str(sp_offset - 4*(i+1))+ "($sp)\n")
                    
                    # INT[INDEX]
                    else:
                        eval_int_array(child, f, var_dict, abs_sp_offset)
                        
                        # Store Value in address $a2 in RAM 
                        f.write("lw $a2 0($a2)\n")                                                         
                        f.write("sw $a2 " + str(sp_offset - 4*(i+1))+ "($sp)\n")
                    
                    operands.append(sp_offset - 4 * (i+1))
                    eval_method.append(2)
                
                # INT VARIABLE
                else:
                    value = var_dict[value]
                    operands.append(abs_sp_offset - value)
                    eval_method.append(1)

    # Load operands in temporal registries $t0 and $t1
    for i in range(len(node.children)):
        
        
        child = node.children[i]
        # Integer literal
        if eval_method[i] == 0:        
            f.write("li $t" + str(i) + " " + str(operands[i]) + "\n")
        
        # Variable or intermediate expression stored in RAM   
        elif eval_method[i] == 1:
            f.write("lw $t" + str(i) + " " + str(operands[i]) +"($sp)\n")
            
        # Int[] 
        else:
            f.write("lw $t" + str(i) + " " + str(operands[i]) +"($sp)\n")

    f.write(arithmetic_dict[node.value]+ " $a0 $t0 $t1\n")
    f.write("sw $a0 " + str(sp_offset) + "($sp)\n")         # Store in main memory
