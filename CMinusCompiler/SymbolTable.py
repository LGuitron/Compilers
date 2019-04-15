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
        elif name in self.parentTable.dictionary:
            return self.parentTable.dictionary[name]
        
        # Return None if it does not exist
        print("ERROR: la variable", name, "no fue declarada en", self.scopeName )
        return None
    
    def __str__(self):
        return_str = "\n"
        for key, value in self.dictionary.items():
            return_str += str(key) + " : " + str(value) + "\n"
        return_str += "\n"    
        
        # Print children symbol tables
        for i in range(len(self.childTables)):
            child = self.childTables[i]
            return_str += "Scope " + str(i+1) + "\n"
            return_str += str(child)
        
        return return_str

    # Create a new child and return it
    def addChild(self, new_child):
        self.childTables.append(new_child)
