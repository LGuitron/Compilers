# Function for adding all runtime errors and program end
def add_runtime_errors(f):

    # PROGRAM END 
    f.write("\nEnd:\nli $v0 10\nsyscall\n")
    errorMessage("Negindexerror", "negindex", f)
    errorMessage("Outboundserror", "outbounds", f)


# Helper function to add runtime error with a message from a data section address
def errorMessage(sectionName,  address, f):
    
    f.write(str(sectionName) + ":\n")
    f.write("li $v0 4\n")
    f.write("la $a0 " + str(address) + "\n")
    f.write("syscall\n")
    f.write("j End\n")
