# Class for symbol table data srtucture
class SymbolTable:
    
    
    def __init__(self, parentTable = None):
        self.dictionary  = {}
        self.parentTable = parentTable  # Store parentTable
        self.childTables = []           # List storing all children for this symbol table
        
    # Add new entry to symbol table
    # TODO show line of ERROR in case of redeclaration
    def insert(self, _name, _type, _property_dict):
        if _name in self.dictionary:
            print("ERROR: Redeclaración de la variable ", _name, " en este scope")
        self.dictionary[_name] = (_type, _property_dict)
    
    def lookup(self, name):
        return self.dictionary[name]
    
    def __str__(self):
        return_str = ""
        for key, value in self.dictionary.items():
            return_str += str(key) + " : " + str(value) + "\n"
            
        # Print children symbol tables
        for i in range(len(self.childTables)):
            child = self.childTables[i]
            return_str += "Scope " + str(i+1) + "\n"
            return_str += str(child)
            return_str += "\n"
        
        return return_str

    # Create a new child and return it
    def addChild(self, new_child):
        self.childTables.append(new_child)
