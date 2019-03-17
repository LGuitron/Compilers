from TreeNode import TreeNode
from globalTypes import *
from cMinusPlyLexer import *
from lexer import *

# This class is used for temporarily saving the lexer before 
# performing production rules where there are various alternatives
class SyntaxAnalyzer:
    
    
    def __init__(self):

        # Lexer information used for error recovery
        lexer            = getLexerObject()
        self.lex_data    = lexer.__dict__['lexdata']
        self.lex_error   = False         # Variable to check if an error in the lexer was found
        self.parse_error = False         # Variable to check if there was a parser error
        
        self.current_token   = 0      # Current index to be seen in the list of tokens
        self.saved_token     = 0      # Saved index to be used for backtracking
        self.tokens          = []     # Array storing all tokens seen
        self.line_numbers    = []     # Array of line numbers for each token seen
        self.token_positions = []     # Array storing position of all tokens in the source code
        
        # Add all tokens to the array
        token, tokenString = getToken(False)
        self.tokens.append((token, tokenString))
        self.line_numbers.append(lexer.__dict__['lineno'])
        self.token_positions.append(lexer.__dict__['lexpos'])
        while (token != TokenType.ENDFILE):
            token, tokenString = getToken(False)
            self.line_numbers.append(lexer.__dict__['lineno'])
            self.token_positions.append(lexer.__dict__['lexpos'])
            self.tokens.append((token, tokenString))
            if(token == TokenType.ERROR):
                self.lex_error = True
        
        # End program execution if there were errors in the lexer
        if self.lex_error:
            exit()
            

    '''
    1. program -> declaration-list
    '''
    def program(self):
        return self.declaration_list()


    '''
    2. declaration-list -> declaration {declaration}
    '''
    def declaration_list(self):
        
        AST = TreeNode("declaration_list")
        AST.addChild(self.declaration())
        while self.current_token < len(self.tokens) - 1:
            AST.addChild(self.declaration())
        
        if not self.parse_error:
            return AST
        return None

    '''
    3. declaration -> var-declaration | fun-declaration
    '''
    def declaration(self):
        
        
        self.saved_token = self.current_token
        declaration = self.var_declaration()

        # Try with function declaration and reset position of checked token
        if declaration is None:
            self.current_token = self.saved_token
            declaration        = self.fun_declaration()
        
        
        if declaration is None:
            self.errorRecovery()
        
        return declaration
    
    '''
    4. var-declaration -> type-specifier ID [ \[ NUM \] ] ;
    '''
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
                        
                        # Check for semicolon
                        if self.match([TokenType.SEMICOLON]) is not None:
                            return node
                        
                # Check for semicolon
                elif self.match([TokenType.SEMICOLON]) is not None:
                    return node

        return None
    
    '''
    5. type-specifier -> int | void
    '''
    def type_specifier(self):
        matched_token = self.match([TokenType.INT, TokenType.VOID])
        if matched_token is not None:
            return matched_token[1]
        return None    

    '''
    6. fun-declaration -> type-specifier ID \( params \) compound-stmt
    '''
    def fun_declaration(self):
        
        node = TreeNode("fun_declaration")
        type_spec = self.type_specifier()

        # Check for type specifier
        if type_spec is not None:
            node.addChild(TreeNode(type_spec))

            # Check for identifier
            matched_identifier = self.match([TokenType.ID])
            if matched_identifier is not None:
                node.addChild(TreeNode(matched_identifier[1]))
                
                # Check for parameters ( params )
                if self.match([TokenType.LPAREN]) is not None:
                    params_node = self.params()
                    if params_node is not None and self.match([TokenType.RPAREN]) is not None:
                        node.addChild(params_node)

                        # Check for function compound statement
                        compound_statement = self.compound_stmt()
                        if compound_statement is not None:
                            node.addChild(compound_statement)
                            return node
        return None

    '''
    7. params -> param-list | void
    '''
    def params(self):

        # Check for param_list
        self.saved_token = self.current_token
        params_node = self.param_list()
        if params_node is not None:
            return params_node
        
        # Check for void parameters
        self.current_token = self.saved_token
        matched_params = self.match([TokenType.VOID])
        if matched_params is not None:
            params_node = TreeNode("param")
            params_node.addChild(TreeNode(matched_params[1]))
            return params_node
        return None
    
    '''
    8. param_list -> param {, param}
    '''
    def param_list(self):
        
        params_node = TreeNode("params")
        new_param   = self.param()
        
        if new_param is not None:
            params_node.addChild(new_param)
        else:
            return None
        
        while self.match([TokenType.COMMA]):
            new_param = self.param()
            if new_param is not None:
                params_node.addChild(new_param)
            else:
                return None
        return params_node
    
    '''
    9. param -> type-specifier ID [ \[ \] ]
    '''
    def param(self):
        
        node = TreeNode("param")
        type_spec = self.type_specifier()
        
        # Check for type specifier
        if type_spec is not None:
            node.addChild(TreeNode(type_spec))
            
            # Check for identifier
            matched_identifier = self.match([TokenType.ID])
            if matched_identifier is not None:
                node.addChild(TreeNode(matched_identifier[1]))
                
                # Check for optional array declaration []
                if self.match([TokenType.LBRACKET]) is not None and self.match([TokenType.RBRACKET]) is not None:
                    node.addChild(TreeNode("[]"))
                    return node
                        
                # Return node
                else:
                    return node
        return None

    '''
    10. compound_stmt -> \{ local-declarations statement-list \}
    '''
    def compound_stmt(self):
        
        node = TreeNode("compound_statement")
        
        # Check for left key
        if self.match([TokenType.LKEY]) is not None:
            
            # Check for local_declarations
            local_vars = self.local_declarations()
            if local_vars is not None:
                node.addChild(local_vars)
            
            
            # Check for statement_list
            #stmt_list = self.statement_list()
            #if stmt_list is not None:
            #    node.addChild(stmt_list)
            
            # Check for right key
            if self.match([TokenType.RKEY]) is not None:
                return node
        
        return None
    
    '''
    11. local_declarations -> {var_declaration}
    '''
    def local_declarations(self):

        node = None
        new_var = self.var_declaration()

        if new_var is not None:
            node = TreeNode("local_declarations")
            
        while new_var is not None:
            node.addChild(new_var)
            new_var = self.var_declaration()
        
        return node
    
    '''
    12. statement_list -> {statement}
    '''
    def statement_list(self):
        
        node = None
        new_stmt = self.statement()

        if new_stmt is not None:
            node = TreeNode("statement_list")
            
        while new_stmt is not None:
            node.addChild(new_stmt)
            new_stmt = self.statement()
        
        return node
        
    
    # TODO finish this
    '''
    13. statement -> expression_stmt | compound_stmt | selection_stmt | iteration_stmt | return_stmt
    '''
    def statement(self):
        return self.expression_stmt()
        

            
    
    '''
    14. expression_stmt -> 
    '''
    def expression_stmt(self):
        pass
        # Check for optional expression
        #new_expression = self.expression()
        
        # Check for semicolon
        #if self.match([TokenType.SEMICOLON]):
            
    
    
    
    
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
    
    
    '''
    
    Function for Syntax Error Recovery
    
    '''
    def errorRecovery(self, errorMessage = "ERROR de sintaxis"):
        
        self.parse_error  = True
        error_pos         = self.token_positions[self.current_token-1]
        error_line_number = self.line_numbers[self.current_token-1]
        
        
        print("--------------------------------------------------------------------")
        print("Linea ", error_line_number, ": ", errorMessage)
        
        
        # Get position of the conflicting character in the current line
        current_position = error_pos
        while self.lex_data[current_position] != "\n" and current_position > 0:
            current_position -= 1

        if error_line_number == 1:
            error_position = error_pos
        else:
            error_position = error_pos - current_position - 1
        
        # Print error line
        error_line = self.lex_data.split("\n")[error_line_number-1]
        print(error_line)
        
        # Print ^ in the corresponding position
        if error_position == 0:
            print("^")
        else:
            print(" " * (error_position-1) , "^")
        print("--------------------------------------------------------------------")
        
        # Skip all the next tokens until a new line is reached   
        self.current_token += 1
        while self.current_token < len(self.line_numbers) and self.line_numbers[self.current_token] == error_line_number:
            self.current_token += 1
        
        # End program if token array is finished
        if self.current_token >= len(self.tokens):
            exit()
        self.saved_token = self.current_token
