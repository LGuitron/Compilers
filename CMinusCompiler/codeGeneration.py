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

    # Check for raw numbers
    try: 
        value = int(value)
        f.write("li $a0 " + str(value) + "\n")
        
        # Assign all left children to this value
        for i in range(len(node.children)-1):
            child = node.children[i]
            current_sp = var_dict[child.value]
            f.write("sw $a0 " +str(current_sp)+"($sp)"+"\n")
        
    
    # TODO Look for variable name in dictionary to get its location in the $sp
    except ValueError:
        pass
    
