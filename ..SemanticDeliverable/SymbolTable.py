# Class for symbol table data srtucture
class SymbolTable:
    
    
    def __init__(self, parentTable = None, reqReturnVerification = False, scopeName = "Global Scope", returnType = None):
        self.reqReturnVerification = reqReturnVerification  # Boolean to determine if this scope requires a return statement (only function scopes)
        self.returnVerified        = False
        self.scopeName             = scopeName 
        self.returnType            = returnType             # Return Type for this scope 
        self.dictionary            = {}
        self.parentTable           = parentTable            # Store parentTable
        self.childTables           = []                     # List storing all children for this symbol table
        
    # Add new entry to symbol table
    def insert(self, _name, _type, _property_dict):
        if _name in self.dictionary:
            print("Error: Redeclaración de la variable", _name, "en", self.scopeName)
            return True
        self.dictionary[_name] = (_type, _property_dict)
        return False
    
    # Lookup in this table, and lookup in parentTable if there is any
    def lookup(self, name):
        if name in self.dictionary:
            return self.dictionary[name]
        
        # look at parentTable
        parent = self.parentTable
        while parent is not None:
            if name in parent.dictionary:
                return parent.dictionary[name]
            parent = parent.parentTable

        print("Error: la variable", name, "no fue declarada en", self.scopeName )
        return None

    def print_w_indent(self, level):
        return_str = "\n"
        for key, value in self.dictionary.items():
            return_str  += "\t"*level + str(key) + " : " + str(value) + "\n"
        return_str += "\t"*level + "------------------------------------\n"    
        
        # Print children symbol tables
        for i in range(len(self.childTables)):
            child = self.childTables[i]
            return_str += child.print_w_indent(level+1)
        return return_str
    
    def __str__(self):
        return self.print_w_indent(0)
        
    # Create a new child and return it
    def addChild(self, new_child):
        self.childTables.append(new_child)
