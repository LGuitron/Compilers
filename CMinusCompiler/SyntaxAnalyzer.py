from TreeNode import TreeNode
from globalTypes import *
from lexer import *

# This class is used for temporarily saving the lexer before 
# performing production rules where there are various alternatives
class SyntaxAnalyzer:
    
    
    def __init__(self):
        self.saved_token   = 0      # Store position of last saved token (for backtracking)
        self.current_token = 0      # Current index to be seen in the list of tokens
        self.tokens        = []     # Array storing all tokens seen
        
        
        # Add all tokens to the array
        token, tokenString = getToken(False)
        self.tokens.append((token, tokenString))
        while (token != TokenType.ENDFILE):
            token, tokenString = getToken(False)     
            self.tokens.append((token, tokenString))
        
    
    def program(self):
        return self.declaration_list()


    def declaration_list(self):
        
        AST = TreeNode("declaration_list")
        AST.addChild(self.declaration())
        while self.current_token < len(self.tokens) - 1:
            AST.addChild(self.declaration())
            #print(self.current_token)
        return AST


    def declaration(self):
        
        
        #self.current_token += 1
        #return self.tokens[self.current_token-1][1]
        
        
        # TODO fun-declaration
        return self.var_declaration()
    
    def var_declaration(self):
        
        node = TreeNode("var_declaration")
        type_spec = self.type_specifier()
        
        # Check for type specifier
        if type_spec is not None:
            node.addChild(type_spec)
            
            # Check for identifier
            if self.tokens[self.current_token][0] == TokenType.ID:
                identifier = self.tokens[self.current_token][1]
                node.addChild(TreeNode(identifier))
                self.current_token += 1

                # Check for semicolon
                if self.tokens[self.current_token][0] == TokenType.SEMICOLON:
                    self.current_token += 1
                    return node
        return None
            
            
    def type_specifier(self):
        if self.tokens[self.current_token][0] == TokenType.INT or self.tokens[self.current_token][0] == TokenType.VOID:
            type_spec = self.tokens[self.current_token][1]
            self.current_token += 1
            return TreeNode(type_spec)
        return None
        
            
        
        
        
