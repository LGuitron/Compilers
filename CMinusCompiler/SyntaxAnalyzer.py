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
        
        declaration = self.var_declaration()

        # Try with function declaration and reset position of checked token
        if declaration is None:
            self.current_token = self.saved_token
            declaration        = self.fun_declaration()
        
        return declaration
    
    def var_declaration(self):
        
        node = TreeNode("var_declaration")
        type_spec = self.type_specifier()
        
        # Check for type specifier
        if type_spec is not None:
            node.addChild(TreeNode(type_spec))
            
            # Check for identifier
            matched_identifier = self.match([TokenType.ID])
            if matched_identifier is not None:
                node.addChild(TreeNode(matched_identifier[1]))


                # Check for optional array declaration [ NUM ]
                if self.match([TokenType.LBRACKET]) is not None:
                    matched_number = self.match([TokenType.NUM])
                    if matched_number is not None and self.match([TokenType.RBRACKET]) is not None:
                        node.addChild(TreeNode("[" + str(matched_number[1]) + "]"))
                    
                    # TODO Error recovery for bad array declaration
                    else:
                        return None
                    
                # Check for semicolon
                if self.match([TokenType.SEMICOLON]) is not None:
                    return node

        return None
    
    # TODO finish this
    def fun_declaration(self):
        
        node = TreeNode("fun_declaration")
        type_spec = self.type_specifier()

        # type-specifier ID \( params \) compound-stmt

        # Check for type specifier
        if type_spec is not None:
            node.addChild(type_spec)
            
        return None
        
        
        pass
    
    
    def type_specifier(self):
        matched_token = self.match([TokenType.INT, TokenType.VOID])
        if matched_token is not None:
            return matched_token[1]
        return None    


    '''
    
    Helper function for matching tokens
    
    '''
    # Check if the next lexer token matches any of the production_tokens specified if a match was found increase value of current token by 1
    # Returns:
    # (token, tokenString) tuple if there was a match
    # None otherwise
    def match(self, production_tokens):
        
        for production_token in production_tokens:
            if self.tokens[self.current_token][0] == production_token:
                self.current_token += 1
                return self.tokens[self.current_token-1]
        return None
        
            
        
        
        
