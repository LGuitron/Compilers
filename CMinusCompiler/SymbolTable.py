# Class for symbol table data srtucture
class SymbolTable:
    
    
    def __init__(self, parentTable = None, scopeName = "Global Scope"):
        self.scopeName  = scopeName 
        self.dictionary  = {}
        self.parentTable = parentTable  # Store parentTable
        self.childTables = []           # List storing all children for this symbol table
        
    # Add new entry to symbol table
    def insert(self, _name, _type, _property_dict):
        if _name in self.dictionary:
            print("ERROR: Redeclaración de la variable", _name, "en", self.scopeName)
            return True
        self.dictionary[_name] = (_type, _property_dict)
        return False
    
    # Lookup in this table, and lookup in parentTable if there is any
    def lookup(self, name):
        if name in self.dictionary:
            return self.dictionary[name]
        
        # look at parentTable
        elif self.parentTable is not None in self.parentTable.dictionary:
            return self.parentTable.dictionary[name]
        
        # Return None if it does not exist
        print("ERROR: la variable", name, "no fue declarada en", self.scopeName )
        return None

    def print_w_indent(self, level):
        return_str = "\n"
        for key, value in self.dictionary.items():
            temp_str     = "\t"*level + str(key)
            temp_str     = temp_str[:-1]
            return_str  += temp_str + " : " + str(value) + "\n"
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
