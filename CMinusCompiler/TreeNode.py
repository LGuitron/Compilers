class TreeNode:
    
    def __init__(self, value):
        self.value    = value
        self.children = []
        
    def addChild(self, childNode):
        self.children.append(childNode)
        
    def __str__(self):
        return self.nodeString(0)
        
    # Print function that keeps track of indentation
    def nodeString(self, indent):
        ret_string = "\t"*indent + self.value + "\n"
        for child in self.children:
            ret_string += child.nodeString(indent+1)
        return ret_string
