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
        self.error_token     = 0      # Save position of latest token seen for identifying error positions
        self.tokens          = []     # Array storing all tokens seen
        self.line_numbers    = []     # Array of line numbers for each token seen
        self.token_positions = []     # Array storing position of all tokens in the source code
        self.key_balance     = 0      # Count extra amount of lkeys compared to rkeys for error recovery
        
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
        
        
        saved_token = self.current_token
        declaration = self.var_declaration()

        # Try with function declaration and reset position of checked token
        if declaration is None:
            error_token   = self.current_token
            self.current_token = saved_token
            declaration        = self.fun_declaration()
        
            # ERROR, the declaration was unsuccesful
            if declaration is None:
                self.current_token = max(error_token, self.current_token, self.error_token)
                self.errorRecovery()
                return None
        return declaration
    
    '''
    4. var-declaration -> type-specifier ID [ \[ NUM \] ] ;
    '''
    def var_declaration(self):
        
        #node = TreeNode("var_declaration")
        type_spec = self.type_specifier()
        
        # Check for type specifier
        if type_spec is not None:
            
            node = TreeNode(type_spec)
            
            # Check for identifier
            matched_identifier = self.match([TokenType.ID])
            if matched_identifier is not None:
                node.addChild(TreeNode(matched_identifier[1]))


                # Check for optional array declaration [ NUM ]
                if self.match([TokenType.LBRACKET]) is not None:
                    matched_number = self.match([TokenType.NUM])
                    if matched_number is not None and self.match([TokenType.RBRACKET]) is not None:
                        
                        node.addChild(TreeNode(str(matched_number[1])))
                        
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
                            #for child in compound_statement:
                                #node.addChild(child)
                            return node
        return None

    '''
    7. params -> param-list | void
    '''
    def params(self):

        error_token = self.current_token

        # Check for param_list
        saved_token = self.current_token
        params_node = self.param_list()
        if params_node is not None:
            return params_node
        error_token = max(error_token, self.current_token)
        
        # Check for void parameters
        self.current_token = saved_token
        matched_params = self.match([TokenType.VOID])
        if matched_params is not None:
            params_node = TreeNode(matched_params[1])
            return params_node
        self.error_token = max(error_token, self.current_token, self.error_token)
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

        type_spec = self.type_specifier()
        
        # Check for type specifier
        if type_spec is not None:
            
            # Check for identifier
            matched_identifier = self.match([TokenType.ID])
            if matched_identifier is not None:
                
                # Check for optional array declaration []
                if self.match([TokenType.LBRACKET]) is not None and self.match([TokenType.RBRACKET]) is not None:
                    node = TreeNode(type_spec + "[]")
                    node.addChild(TreeNode(matched_identifier[1]))
                        
                # Return node
                else:
                    node = TreeNode(type_spec)
                    node.addChild(TreeNode(matched_identifier[1]))
                return node
        return None

    '''
    10. compound_stmt -> \{ local-declarations statement-list \}
    '''
    def compound_stmt(self):

        # Declare array of children for the compound statement
        node = TreeNode("compound_statement")
        nodes = None
        
        # Check for left key
        if self.match([TokenType.LKEY]) is not None:
            
            nodes = []
            
            # Check for local_declarations
            local_vars = self.local_declarations()
            if local_vars is not None:
                
                #Add each child of the local declaration as child of the compound_stmt
                for child in local_vars:
                    node.addChild(child)
                    #nodes.append(child)
            
            # Check for statement_list
            stmt_list = self.statement_list()
            if stmt_list is not None:
                
                # Append each child of statement list as child of the compound_stmt
                for child in stmt_list:
                    node.addChild(child)
                    #nodes.append(child)
                
            # Check for right key
            if self.match([TokenType.RKEY]) is not None:
                return node
                #return nodes
        
        return None
    
    '''
    11. local_declarations -> {var_declaration}
    '''
    def local_declarations(self):

        nodes = None
        new_var = self.var_declaration()

        if new_var is not None:
            nodes = []
            
        while new_var is not None:
            nodes.append(new_var)
            new_var = self.var_declaration()      
        return nodes
    
    '''
    12. statement_list -> {statement}
    '''
    def statement_list(self):

        nodes    = None
        new_stmt = self.statement()

        if new_stmt is not None:
            nodes = []
            
        while new_stmt is not None:
            # In case of a compound statement add every individual child
            if type(new_stmt) == list:
                for child in new_stmt:
                    nodes.append(child)
            # Otherwise add the statement by itself
            else:
                nodes.append(new_stmt)
            new_stmt = self.statement()
        
        return nodes

    '''
    13. statement -> expression_stmt | compound_stmt | selection_stmt | iteration_stmt | return_stmt
    '''
    def statement(self):
        
        saved_token = self.current_token
        error_token = self.current_token
        
        # Check for expression_stmt
        expr = self.expression_stmt()
        if expr is not None:
            return expr
        error_token = max(error_token, self.current_token)
        
        # Check for compound_stmt (return value here is a list)
        self.current_token = saved_token
        expr = self.compound_stmt()
        if expr is not None:
            return expr
        error_token = max(error_token, self.current_token)
        
        # Check for selection_stmt
        self.current_token = saved_token
        expr = self.selection_stmt()
        if expr is not None:
            return expr
        error_token = max(error_token, self.current_token)
        
        # Check for iteration_stmt
        self.current_token = saved_token
        expr = self.iteration_stmt()
        if expr is not None:
            return expr
        error_token = max(error_token, self.current_token)
    
        # Check for return_stmt
        self.current_token = saved_token
        expr = self.return_stmt()
        if expr is not None:
            return expr
        self.error_token = max(error_token, self.current_token, self.error_token)
        
        # Error detected, update value of current error to detect it properly 
        return None

    '''
    14. expression_stmt -> [expression] ;
    '''
    def expression_stmt(self):

        # Check for optional expression
        new_expression = self.expression()
        
        # Check for semicolon
        if new_expression is not None and self.match([TokenType.SEMICOLON]) is not None:
            return new_expression
        return None

    '''
    15. selection_stmt -> if (expression) statement [else statement]
    '''
    def selection_stmt(self):
        
        
        # Check for if token
        if self.match([TokenType.IF]) is not None:
            node = TreeNode("if")
            
            # Check for (expression)
            if self.match([TokenType.LPAREN]) is not None:
                new_expression = self.expression()
                if new_expression is not None and self.match([TokenType.RPAREN]) is not None:
                    node.addChild(new_expression)
                    if_statement = self.statement()
                    if if_statement is not None:
                        
                        # In case of a compound statement add every individual child
                        if type(if_statement) == list:
                            for child in if_statement:
                                node.addChild(child)
                        # Otherwise add the if statement by itself
                        else:
                            node.addChild(if_statement)
                    
                        # Check for optional else clause
                        if self.match([TokenType.ELSE]) is not None:
                            else_statement = self.statement()
                            
                            if else_statement is not None:
                                
                                # In case of a compound statement add every individual child
                                if type(else_statement) == list:
                                    for child in else_statement:
                                        node.addChild(child)
                                # Otherwise add the else statement by itself
                                else:
                                    node.addChild(else_statement)
                        
                            # Error, expected an expression here after seeing else
                            else:
                                return None
                    
                    return node
        return None
        

    '''
    16. iteration_stmt -> while (expression) statement
    '''
    def iteration_stmt(self):

        # Check for while token
        if self.match([TokenType.WHILE]) is not None:
            node = TreeNode("while")
            
            # Check for (expression)
            if self.match([TokenType.LPAREN]) is not None:
                new_expression = self.expression()
                if new_expression is not None and self.match([TokenType.RPAREN]) is not None:
                    node.addChild(new_expression)
                    while_statement = self.statement()
                    if while_statement is not None:

                        # In case of a compound statement add every individual child
                        if type(while_statement) == list:
                            for child in while_statement:
                                node.addChild(child)
                        # Otherwise add the else statement by itself
                        else:
                            node.addChild(while_statement)
                        return node
        return None
    

    '''
    17. return_stmt -> return [expression];
    '''
    def return_stmt(self):
        
        # Check for return token
        if self.match([TokenType.RETURN]) is not None:
            node = TreeNode("return")
            
            # Check for optional expression
            saved_token = self.current_token
            new_expression = self.expression()
            if new_expression is not None:
                node.addChild(new_expression)
            
            # If no expression was found restore the current token
            else:
                self.current_token = saved_token
                
            # Look for semicolon token
            if self.match([TokenType.SEMICOLON]) is not None:
                return node
        return None

    '''
    18. expression -> {var =} simple expression
    '''
    def expression(self):
        node = None
            
        # Look for optional var assignments, token position is saved before looking for more vars
        saved_token = self.current_token
        new_var = self.var()

        while new_var is not None:
            
            # Look for equals sign after this var
            if self.match([TokenType.EQUALS]):
                
                # Create root node for equals operator if this is the first one seen
                if node is None:
                    node = TreeNode("=")
                
                node.addChild(new_var)
                saved_token = self.current_token
                new_var = self.var()
                
            # Break the loop (maybe this is a function call)
            else:
                break
        self.current_token = saved_token
        
        # Check for simple_expression
        simple_expr = self.simple_expression()
        if simple_expr is not None:
            
            # Check wheter to add a child node or create a new node
            if node is None:
                return simple_expr
            else:
                node.addChild(simple_expr)
                return node
            
        else:
            return None

    '''
    19. var -> ID [ \[ expression \] ]
    '''
    def var(self):

        matched_identifier = self.match([TokenType.ID])
        if matched_identifier is not None:
            
            node = TreeNode(matched_identifier[1])

            # Check for optional expression in array syntax
            if self.match([TokenType.LBRACKET]) is not None:
                
                new_expression = self.expression()
                if new_expression is not None and self.match([TokenType.RBRACKET]) is not None:
                    node.addChild(new_expression)
                    return node

            else:
                return node
        return None

    '''
    20. simple_expression -> additive_expression [relop additive_expression]
    '''
    def simple_expression(self):

        # Check for first additive_expression
        add_exp = self.additive_expression()
        if add_exp is not None:

            # Single additive expression
            matched_operator = self.relop()
            if matched_operator is None:
                node = add_exp
            
            # Found relation operator, set it as the node and set its 2 children accordingly
            else:
                node = TreeNode(matched_operator)
                node.addChild(add_exp)
                add_exp = self.additive_expression()
                
                # Look for additive expression at right side
                if add_exp is not None:
                    node.addChild(add_exp)
                else:
                    return None
                
            #else:
            return node

        return None
    
    '''
    21. relop -> <= | < | > | >= | == | !=
    '''
    def relop(self):
        matched_token = self.match([TokenType.LT, TokenType.LE,TokenType.GT, TokenType.GE, TokenType.EQ, TokenType.NE ])
        if matched_token is not None:
            return matched_token[1]
        return None   

    '''
    22. additive_expression -> term {addop term}
    '''
    def additive_expression(self):
        
        # Check for first term
        term = self.term()
        if term is not None:
            
            matched_operator = self.addop()
            if matched_operator is None:
                node = term
            
            # Set additive operator as the root
            else:
                node = TreeNode(matched_operator)
                node.addChild(term)
            
            while matched_operator is not None:
                
                # Get the term on the right side of the operator
                term = self.term()
                if term is not None:
                    
                    # Add factor as right child of the current node
                    node.addChild(term)

                    # Check if there is another operator to the right
                    matched_operator = self.addop()
                    if matched_operator is not None:
                        parentNode = TreeNode(matched_operator)  # New operator to the right becomes the parent of the current node
                        parentNode.addChild(node)                # Add current node as left child of the new parent
                        node = parentNode                        # Update current node as the parent of the last
                else:
                    return None
            return node
        return None

    
    '''
    23. addop -> + | -
    '''
    def addop(self):
        matched_token = self.match([TokenType.PLUS, TokenType.MINUS])
        if matched_token is not None:
            return matched_token[1]
        return None 

    '''
    24. term -> factor {mulop factor}
    '''
    def term(self):
        factor = self.factor()
    
        if factor is not None:

            matched_operator = self.mulop()
        
            # If there are no operations to the right return tha factor value as the node
            if matched_operator is None:
                node = factor
            
            # Set mult_operator as the root
            else:
                node = TreeNode(matched_operator)
                node.addChild(factor)
            
            #currentNode = node
            while matched_operator is not None:

                # Get the factor on the right side of the operator
                factor = self.factor()
                if factor is not None:
                    
                    # Add factor as right child of the current node
                    node.addChild(factor)

                    # Check if there is another operator to the right
                    matched_operator = self.mulop()
                    if matched_operator is not None:
                        parentNode = TreeNode(matched_operator)  # New operator to the right becomes the parent of the current node
                        parentNode.addChild(node)                # Add current node as left child of the new parent
                        node = parentNode                        # Update current node as the parent of the last
                else:
                    return None
            return node
        return None
    
    
    '''
    25. mulop -> * | /
    '''
    def mulop(self):
        matched_token = self.match([TokenType.TIMES, TokenType.DIVIDE])
        if matched_token is not None:
            return matched_token[1]
        return None 

    '''
    26. factor -> NUM | (expression) | call | var
    '''
    def factor(self):

        saved_token = self.current_token
        error_token = self.current_token
        
        # Check for NUM
        matched_num = self.match([TokenType.NUM])
        if matched_num is not None:
            return TreeNode(str(matched_num[1]))
        error_token = max(error_token, self.current_token)

        # Check for ( expression )
        if self.match([TokenType.LPAREN]) is not None:
            factor = self.expression()
            if factor is not None and self.match([TokenType.RPAREN]) is not None:
                return factor
        error_token = max(error_token, self.current_token)
        
        # check for call
        self.current_token = saved_token
        factor = self.call()
        if factor is not None:
            return factor
        error_token = max(error_token, self.current_token)

        # Check for var
        self.current_token = saved_token
        factor = self.var()
        if factor is not None:
            return factor
        self.error_token = max(error_token, self.current_token, self.error_token)
        return None
    
    '''
    27. call -> ID (args)
    '''
    def call(self):
        
        matched_identifier = self.match([TokenType.ID]) 
        if matched_identifier is not None:
            node = TreeNode(matched_identifier[1])
            if self.match([TokenType.LPAREN]) is not None:
                arguments = self.args()
                if arguments is not None and self.match([TokenType.RPAREN]) is not None:
                    node.addChild(arguments)
                    return node
        return None
    
    
    '''
    28. args -> arg-list | epsilon
    '''
    def args(self):
        
        args = self.arg_list()
        
        # Check for arglist
        saved_token = self.current_token
        if args is not None:
            return args

        # Restore token and Return an empty TreeNode for epsilon
        self.current_token = saved_token
        node = TreeNode("args")
        node.addChild(TreeNode("void"))
        return node
    
    '''
    29. arg_list -> expression {, expression}
    '''
    def arg_list(self):
        
        node = TreeNode("args")
        
        # Look for first expression
        new_expression = self.expression()
        if new_expression is not None:

            node.addChild(new_expression)
        
            # Look for additional expressions separated by commas
            while self.match([TokenType.COMMA]) is not None:
                new_expression = self.expression()
                if new_expression is not None:
                    node.addChild(new_expression)
                else:
                    return None
            return node
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
                
                # Change balance counter for keys when necessary
                if production_token == TokenType.LKEY:
                    self.key_balance += 1
                elif production_token == TokenType.RKEY:
                    self.key_balance -= 1
                    self.key_balance = max(0, self.key_balance)
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
        
        # Go back until the last character is not a \n
        while self.lex_data[current_position] == "\n" and current_position > 0:
            current_position -= 1
        
        # Go back until the last character is a \n
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

        
        '''
        Attempt to get out of the current function (if in a function)
        '''
        temp_token = self.current_token
        
        
        # Skip all tokens until reaching a point were opening and closing keys { } are balanced
        temp_token += 1
        for i in range(self.key_balance, 0, -1):
            
            while temp_token < len(self.line_numbers) and self.tokens[temp_token][0] != TokenType.RKEY:
                temp_token += 1
            temp_token += 1
        
        '''
        If the key balance was already 0 attempt to get out of statement (look for semicolon)
        '''
        if self.key_balance == 0:
        
            self.current_token += 1
            while self.current_token < len(self.line_numbers) and self.tokens[self.current_token][0] != TokenType.SEMICOLON:
                self.current_token += 1
            
            # Skip all the next tokens until a token different than a semicolon is reached
            while self.current_token < len(self.line_numbers) and self.tokens[self.current_token][0] == TokenType.SEMICOLON:
                self.current_token += 1

        else:
            self.current_token = temp_token
        self.key_balance = 0
