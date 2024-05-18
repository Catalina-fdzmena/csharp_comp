
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocLTLEGTGEleftPLUSMINUSleftMULTDIVIDEMODrightNOTrightINCREMENTDECREMENTleftANDORAND ARROW BOOL BOOLCONST BOOLEQUAL BREAK CHAR CHARCONST COLON COMMA COMMENT CONST DECREMENT DIVIDE DO DOT DOUBLE DOUBLECONST ELSE EQUAL FALSE FLOAT FLOATCONST FOR FOREACH GE GT ID IF INCREMENT INT INTCONST LBRACE LBRACKET LE LONG LONGCONST LPAREN LT MINUS MINUSEQUAL MOD MULT MULTILINECOMMENT NE NEW NOT OR PLUS PLUSEQUAL PRIVATE PROGRAM PUBLIC RBRACE RBRACKET RETURN RPAREN STMT_TERMINATOR STRCONST STRING THEN TRUE VOID WHILE WRITE WRITELNprogramstart : PROGRAM ID LBRACE code RBRACEcode : statementcode : code statementstatement : assignment STMT_TERMINATOR\n                 | declaration STMT_TERMINATOR\n                 | expression STMT_TERMINATOR\n                 | if_statement\n                 | while_statement\n                 | for_statement\n                 | array_declaration STMT_TERMINATOR\n                 | array_assignment STMT_TERMINATOR\n                 | write_statement\n                 | writeln_statement\n                 | break_statement\n                 | return_statementdeclaration : datatype declareiddeclareid : IDdeclareid : assignmentdeclareid : declareid COMMA IDdeclareid : declareid COMMA assignmentassignment : ID EQUAL expression\n                  | ID PLUSEQUAL expression\n                  | ID MINUSEQUAL expressiondatatype : INT\n                | FLOAT\n                | BOOL\n                | CHAR\n                | DOUBLE\n                | LONG\n                | STRINGexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term MULT factorterm : term DIVIDE factorterm : factorfactor : ID\n              | INTCONST\n              | FLOATCONST\n              | DOUBLECONST\n              | LONGCONST\n              | BOOLCONST\n              | STRCONST\n              | CHARCONST\n              | array_accessfactor : LPAREN expression RPARENexpression : expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression NE expression\n                  | expression BOOLEQUAL expressionexpression : expression AND expression\n                  | expression OR expressionexpression : ID INCREMENTexpression : ID DECREMENTassignment : ID INCREMENT STMT_TERMINATORassignment : ID DECREMENT STMT_TERMINATORexpression : expression ARROW IDif_statement : IF LPAREN expression RPAREN LBRACE code RBRACE\n                    | IF LPAREN expression RPAREN LBRACE code RBRACE ELSE LBRACE code RBRACEwhile_statement : WHILE LPAREN expression RPAREN LBRACE code RBRACEfor_statement : FOR LPAREN assignment STMT_TERMINATOR expression STMT_TERMINATOR expression RPAREN LBRACE code RBRACEarguments : expression\n                 | arguments COMMA expression\n                 | emptyarray_declaration : datatype ID LBRACKET INTCONST RBRACKETarray_assignment : ID LBRACKET expression RBRACKET EQUAL expressionarray_access : ID LBRACKET expression RBRACKETwrite_statement : WRITE LPAREN expression RPAREN STMT_TERMINATORwriteln_statement : WRITELN LPAREN expression RPAREN STMT_TERMINATORbreak_statement : BREAK STMT_TERMINATORreturn_statement : RETURN expression STMT_TERMINATOR\n                        | RETURN STMT_TERMINATORempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,52,],[0,-1,]),'ID':([2,4,6,7,11,12,13,16,17,18,19,20,23,30,31,32,33,34,35,36,37,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,74,75,78,79,80,81,82,84,103,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[3,5,5,-2,-7,-8,-9,-12,-13,-14,-15,71,77,77,-24,-25,-26,-27,-28,-29,-30,77,77,77,77,-3,-4,-5,-6,92,92,77,77,77,77,77,77,77,77,102,-10,-11,92,92,77,77,116,77,77,-72,-74,121,77,-73,77,77,5,5,-70,-71,5,5,77,-60,-62,5,5,5,5,-61,-63,]),'LBRACE':([3,124,126,145,146,],[4,132,134,147,148,]),'IF':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[22,22,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,22,22,-70,-71,22,22,-60,-62,22,22,22,22,-61,-63,]),'WHILE':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[24,24,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,24,24,-70,-71,24,24,-60,-62,24,24,24,24,-61,-63,]),'FOR':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[25,25,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,25,25,-70,-71,25,25,-60,-62,25,25,25,25,-61,-63,]),'WRITE':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[27,27,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,27,27,-70,-71,27,27,-60,-62,27,27,27,27,-61,-63,]),'WRITELN':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[28,28,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,28,28,-70,-71,28,28,-60,-62,28,28,28,28,-61,-63,]),'BREAK':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[29,29,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,29,29,-70,-71,29,29,-60,-62,29,29,29,29,-61,-63,]),'RETURN':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[30,30,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,30,30,-70,-71,30,30,-60,-62,30,30,30,30,-61,-63,]),'INT':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[31,31,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,31,31,-70,-71,31,31,-60,-62,31,31,31,31,-61,-63,]),'FLOAT':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[32,32,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,32,32,-70,-71,32,32,-60,-62,32,32,32,32,-61,-63,]),'BOOL':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[33,33,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,33,33,-70,-71,33,33,-60,-62,33,33,33,33,-61,-63,]),'CHAR':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[34,34,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,34,34,-70,-71,34,34,-60,-62,34,34,34,34,-61,-63,]),'DOUBLE':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[35,35,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,35,35,-70,-71,35,35,-60,-62,35,35,35,35,-61,-63,]),'LONG':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[36,36,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,36,36,-70,-71,36,36,-60,-62,36,36,36,36,-61,-63,]),'STRING':([4,6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,132,134,136,137,139,140,142,143,147,148,149,150,151,152,],[37,37,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,37,37,-70,-71,37,37,-60,-62,37,37,37,37,-61,-63,]),'INTCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,104,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[26,26,-2,-7,-8,-9,-12,-13,-14,-15,26,26,26,26,26,26,-3,-4,-5,-6,26,26,26,26,26,26,26,26,26,26,-10,-11,26,26,26,26,26,26,-72,-74,123,26,-73,26,26,26,26,-70,-71,26,26,26,-60,-62,26,26,26,26,-61,-63,]),'FLOATCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[39,39,-2,-7,-8,-9,-12,-13,-14,-15,39,39,39,39,39,39,-3,-4,-5,-6,39,39,39,39,39,39,39,39,39,39,-10,-11,39,39,39,39,39,39,-72,-74,39,-73,39,39,39,39,-70,-71,39,39,39,-60,-62,39,39,39,39,-61,-63,]),'DOUBLECONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[40,40,-2,-7,-8,-9,-12,-13,-14,-15,40,40,40,40,40,40,-3,-4,-5,-6,40,40,40,40,40,40,40,40,40,40,-10,-11,40,40,40,40,40,40,-72,-74,40,-73,40,40,40,40,-70,-71,40,40,40,-60,-62,40,40,40,40,-61,-63,]),'LONGCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[41,41,-2,-7,-8,-9,-12,-13,-14,-15,41,41,41,41,41,41,-3,-4,-5,-6,41,41,41,41,41,41,41,41,41,41,-10,-11,41,41,41,41,41,41,-72,-74,41,-73,41,41,41,41,-70,-71,41,41,41,-60,-62,41,41,41,41,-61,-63,]),'BOOLCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[42,42,-2,-7,-8,-9,-12,-13,-14,-15,42,42,42,42,42,42,-3,-4,-5,-6,42,42,42,42,42,42,42,42,42,42,-10,-11,42,42,42,42,42,42,-72,-74,42,-73,42,42,42,42,-70,-71,42,42,42,-60,-62,42,42,42,42,-61,-63,]),'STRCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[43,43,-2,-7,-8,-9,-12,-13,-14,-15,43,43,43,43,43,43,-3,-4,-5,-6,43,43,43,43,43,43,43,43,43,43,-10,-11,43,43,43,43,43,43,-72,-74,43,-73,43,43,43,43,-70,-71,43,43,43,-60,-62,43,43,43,43,-61,-63,]),'CHARCONST':([4,6,7,11,12,13,16,17,18,19,23,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[44,44,-2,-7,-8,-9,-12,-13,-14,-15,44,44,44,44,44,44,-3,-4,-5,-6,44,44,44,44,44,44,44,44,44,44,-10,-11,44,44,44,44,44,44,-72,-74,44,-73,44,44,44,44,-70,-71,44,44,44,-60,-62,44,44,44,44,-61,-63,]),'LPAREN':([4,6,7,11,12,13,16,17,18,19,22,23,24,25,27,28,30,46,47,48,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,74,75,78,80,81,82,84,113,119,127,130,132,134,136,137,139,140,141,142,143,147,148,149,150,151,152,],[23,23,-2,-7,-8,-9,-12,-13,-14,-15,75,23,78,79,80,81,23,23,23,23,23,-3,-4,-5,-6,23,23,23,23,23,23,23,23,23,23,-10,-11,23,23,23,23,23,23,-72,-74,23,-73,23,23,23,23,-70,-71,23,23,23,-60,-62,23,23,23,23,-61,-63,]),'EQUAL':([5,71,116,120,121,],[46,46,46,130,46,]),'PLUSEQUAL':([5,71,116,121,],[47,47,47,47,]),'MINUSEQUAL':([5,71,116,121,],[48,48,48,48,]),'INCREMENT':([5,71,77,116,121,],[49,105,111,105,105,]),'DECREMENT':([5,71,77,116,121,],[50,106,112,106,106,]),'LBRACKET':([5,71,77,92,],[51,104,113,113,]),'MULT':([5,21,26,38,39,40,41,42,43,44,45,77,91,92,93,107,108,110,120,133,],[-37,73,-38,-36,-39,-40,-41,-42,-43,-44,-45,-37,73,-37,73,-34,-35,-46,-69,-69,]),'DIVIDE':([5,21,26,38,39,40,41,42,43,44,45,77,91,92,93,107,108,110,120,133,],[-37,74,-38,-36,-39,-40,-41,-42,-43,-44,-45,-37,74,-37,74,-34,-35,-46,-69,-69,]),'STMT_TERMINATOR':([5,8,9,10,14,15,21,26,29,30,38,39,40,41,42,43,44,45,49,50,70,71,72,77,83,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,105,106,107,108,110,111,112,115,120,121,122,128,129,131,133,135,138,],[-37,54,55,56,68,69,-33,-38,82,84,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,-16,-17,-18,-37,119,-21,-22,-23,-57,-58,-31,-37,-32,-47,-48,-49,-50,-51,-52,-53,-54,-59,88,89,-34,-35,-46,-55,-56,127,-69,-19,-20,136,137,-67,-69,141,-68,]),'PLUS':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,57,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,57,-37,57,57,57,57,57,-31,-37,-32,57,57,57,57,57,57,-53,-54,-59,-34,-35,57,-46,-55,-56,57,57,57,-69,57,-69,57,57,57,]),'MINUS':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,58,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,58,-37,58,58,58,58,58,-31,-37,-32,58,58,58,58,58,58,-53,-54,-59,-34,-35,58,-46,-55,-56,58,58,58,-69,58,-69,58,58,58,]),'LT':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,59,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,59,-37,59,59,59,59,59,-31,-37,-32,None,None,None,None,59,59,-53,-54,-59,-34,-35,59,-46,-55,-56,59,59,59,-69,59,-69,59,59,59,]),'GT':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,60,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,60,-37,60,60,60,60,60,-31,-37,-32,None,None,None,None,60,60,-53,-54,-59,-34,-35,60,-46,-55,-56,60,60,60,-69,60,-69,60,60,60,]),'LE':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,61,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,61,-37,61,61,61,61,61,-31,-37,-32,None,None,None,None,61,61,-53,-54,-59,-34,-35,61,-46,-55,-56,61,61,61,-69,61,-69,61,61,61,]),'GE':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,62,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,62,-37,62,62,62,62,62,-31,-37,-32,None,None,None,None,62,62,-53,-54,-59,-34,-35,62,-46,-55,-56,62,62,62,-69,62,-69,62,62,62,]),'NE':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,63,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,63,-37,63,63,63,63,63,-31,-37,-32,-47,-48,-49,-50,63,63,-53,-54,-59,-34,-35,63,-46,-55,-56,63,63,63,-69,63,-69,63,63,63,]),'BOOLEQUAL':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,64,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,64,-37,64,64,64,64,64,-31,-37,-32,-47,-48,-49,-50,64,64,-53,-54,-59,-34,-35,64,-46,-55,-56,64,64,64,-69,64,-69,64,64,64,]),'AND':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,65,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,65,-37,65,65,65,65,65,-31,-37,-32,65,65,65,65,65,65,-53,-54,-59,-34,-35,65,-46,-55,-56,65,65,65,-69,65,-69,65,65,65,]),'OR':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,66,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,66,-37,66,66,66,66,66,-31,-37,-32,66,66,66,66,66,66,-53,-54,-59,-34,-35,66,-46,-55,-56,66,66,66,-69,66,-69,66,66,66,]),'ARROW':([5,10,21,26,38,39,40,41,42,43,44,45,49,50,76,77,83,85,86,87,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,120,125,133,135,138,144,],[-37,67,-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-55,-56,67,-37,67,67,67,67,67,-31,-37,-32,-47,-48,-49,-50,67,67,-53,-54,-59,-34,-35,67,-46,-55,-56,67,67,67,-69,67,-69,67,67,67,]),'RBRACE':([6,7,11,12,13,16,17,18,19,53,54,55,56,68,69,82,84,119,136,137,139,140,142,143,149,150,151,152,],[52,-2,-7,-8,-9,-12,-13,-14,-15,-3,-4,-5,-6,-10,-11,-72,-74,-73,-70,-71,142,143,-60,-62,151,152,-61,-63,]),'RPAREN':([21,26,38,39,40,41,42,43,44,45,76,77,91,92,93,94,95,96,97,98,99,100,101,102,107,108,109,110,111,112,114,117,118,133,144,],[-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,110,-37,-31,-37,-32,-47,-48,-49,-50,-51,-52,-53,-54,-59,-34,-35,124,-46,-55,-56,126,128,129,-69,146,]),'COMMA':([21,26,38,39,40,41,42,43,44,45,70,71,72,77,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,101,102,107,108,110,111,112,121,122,133,],[-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,103,-17,-18,-37,-21,-22,-23,-57,-58,-31,-37,-32,-47,-48,-49,-50,-51,-52,-53,-54,-59,-34,-35,-46,-55,-56,-19,-20,-69,]),'RBRACKET':([21,26,38,39,40,41,42,43,44,45,77,90,91,92,93,94,95,96,97,98,99,100,101,102,107,108,110,111,112,123,125,133,],[-33,-38,-36,-39,-40,-41,-42,-43,-44,-45,-37,120,-31,-37,-32,-47,-48,-49,-50,-51,-52,-53,-54,-59,-34,-35,-46,-55,-56,131,133,-69,]),'ELSE':([142,],[145,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programstart':([0,],[1,]),'code':([4,132,134,147,148,],[6,139,140,149,150,]),'statement':([4,6,132,134,139,140,147,148,149,150,],[7,53,7,7,53,53,7,7,53,53,]),'assignment':([4,6,20,79,103,132,134,139,140,147,148,149,150,],[8,8,72,115,122,8,8,8,8,8,8,8,8,]),'declaration':([4,6,132,134,139,140,147,148,149,150,],[9,9,9,9,9,9,9,9,9,9,]),'expression':([4,6,23,30,46,47,48,51,59,60,61,62,63,64,65,66,75,78,80,81,113,127,130,132,134,139,140,141,147,148,149,150,],[10,10,76,83,85,86,87,90,94,95,96,97,98,99,100,101,109,114,117,118,125,135,138,10,10,10,10,144,10,10,10,10,]),'if_statement':([4,6,132,134,139,140,147,148,149,150,],[11,11,11,11,11,11,11,11,11,11,]),'while_statement':([4,6,132,134,139,140,147,148,149,150,],[12,12,12,12,12,12,12,12,12,12,]),'for_statement':([4,6,132,134,139,140,147,148,149,150,],[13,13,13,13,13,13,13,13,13,13,]),'array_declaration':([4,6,132,134,139,140,147,148,149,150,],[14,14,14,14,14,14,14,14,14,14,]),'array_assignment':([4,6,132,134,139,140,147,148,149,150,],[15,15,15,15,15,15,15,15,15,15,]),'write_statement':([4,6,132,134,139,140,147,148,149,150,],[16,16,16,16,16,16,16,16,16,16,]),'writeln_statement':([4,6,132,134,139,140,147,148,149,150,],[17,17,17,17,17,17,17,17,17,17,]),'break_statement':([4,6,132,134,139,140,147,148,149,150,],[18,18,18,18,18,18,18,18,18,18,]),'return_statement':([4,6,132,134,139,140,147,148,149,150,],[19,19,19,19,19,19,19,19,19,19,]),'datatype':([4,6,132,134,139,140,147,148,149,150,],[20,20,20,20,20,20,20,20,20,20,]),'term':([4,6,23,30,46,47,48,51,57,58,59,60,61,62,63,64,65,66,75,78,80,81,113,127,130,132,134,139,140,141,147,148,149,150,],[21,21,21,21,21,21,21,21,91,93,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'factor':([4,6,23,30,46,47,48,51,57,58,59,60,61,62,63,64,65,66,73,74,75,78,80,81,113,127,130,132,134,139,140,141,147,148,149,150,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,107,108,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'array_access':([4,6,23,30,46,47,48,51,57,58,59,60,61,62,63,64,65,66,73,74,75,78,80,81,113,127,130,132,134,139,140,141,147,148,149,150,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'declareid':([20,],[70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programstart","S'",1,None,None,None),
  ('programstart -> PROGRAM ID LBRACE code RBRACE','programstart',5,'p_programstart','parse.py',20),
  ('code -> statement','code',1,'p_code_singleline','parse.py',25),
  ('code -> code statement','code',2,'p_code_multiple','parse.py',30),
  ('statement -> assignment STMT_TERMINATOR','statement',2,'p_statement_variables','parse.py',36),
  ('statement -> declaration STMT_TERMINATOR','statement',2,'p_statement_variables','parse.py',37),
  ('statement -> expression STMT_TERMINATOR','statement',2,'p_statement_variables','parse.py',38),
  ('statement -> if_statement','statement',1,'p_statement_variables','parse.py',39),
  ('statement -> while_statement','statement',1,'p_statement_variables','parse.py',40),
  ('statement -> for_statement','statement',1,'p_statement_variables','parse.py',41),
  ('statement -> array_declaration STMT_TERMINATOR','statement',2,'p_statement_variables','parse.py',42),
  ('statement -> array_assignment STMT_TERMINATOR','statement',2,'p_statement_variables','parse.py',43),
  ('statement -> write_statement','statement',1,'p_statement_variables','parse.py',44),
  ('statement -> writeln_statement','statement',1,'p_statement_variables','parse.py',45),
  ('statement -> break_statement','statement',1,'p_statement_variables','parse.py',46),
  ('statement -> return_statement','statement',1,'p_statement_variables','parse.py',47),
  ('declaration -> datatype declareid','declaration',2,'p_declaration','parse.py',52),
  ('declareid -> ID','declareid',1,'p_declareid_single','parse.py',57),
  ('declareid -> assignment','declareid',1,'p_declareid_singlev','parse.py',62),
  ('declareid -> declareid COMMA ID','declareid',3,'p_declareid_multiple','parse.py',67),
  ('declareid -> declareid COMMA assignment','declareid',3,'p_declareid_multiplev','parse.py',72),
  ('assignment -> ID EQUAL expression','assignment',3,'p_assignment','parse.py',77),
  ('assignment -> ID PLUSEQUAL expression','assignment',3,'p_assignment','parse.py',78),
  ('assignment -> ID MINUSEQUAL expression','assignment',3,'p_assignment','parse.py',79),
  ('datatype -> INT','datatype',1,'p_datatype','parse.py',84),
  ('datatype -> FLOAT','datatype',1,'p_datatype','parse.py',85),
  ('datatype -> BOOL','datatype',1,'p_datatype','parse.py',86),
  ('datatype -> CHAR','datatype',1,'p_datatype','parse.py',87),
  ('datatype -> DOUBLE','datatype',1,'p_datatype','parse.py',88),
  ('datatype -> LONG','datatype',1,'p_datatype','parse.py',89),
  ('datatype -> STRING','datatype',1,'p_datatype','parse.py',90),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parse.py',94),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parse.py',98),
  ('expression -> term','expression',1,'p_expression_term','parse.py',102),
  ('term -> term MULT factor','term',3,'p_term_multiplication','parse.py',106),
  ('term -> term DIVIDE factor','term',3,'p_term_div','parse.py',110),
  ('term -> factor','term',1,'p_term_factor','parse.py',114),
  ('factor -> ID','factor',1,'p_factor_num','parse.py',118),
  ('factor -> INTCONST','factor',1,'p_factor_num','parse.py',119),
  ('factor -> FLOATCONST','factor',1,'p_factor_num','parse.py',120),
  ('factor -> DOUBLECONST','factor',1,'p_factor_num','parse.py',121),
  ('factor -> LONGCONST','factor',1,'p_factor_num','parse.py',122),
  ('factor -> BOOLCONST','factor',1,'p_factor_num','parse.py',123),
  ('factor -> STRCONST','factor',1,'p_factor_num','parse.py',124),
  ('factor -> CHARCONST','factor',1,'p_factor_num','parse.py',125),
  ('factor -> array_access','factor',1,'p_factor_num','parse.py',126),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','parse.py',130),
  ('expression -> expression LT expression','expression',3,'p_expression_relop','parse.py',135),
  ('expression -> expression GT expression','expression',3,'p_expression_relop','parse.py',136),
  ('expression -> expression LE expression','expression',3,'p_expression_relop','parse.py',137),
  ('expression -> expression GE expression','expression',3,'p_expression_relop','parse.py',138),
  ('expression -> expression NE expression','expression',3,'p_expression_relop','parse.py',139),
  ('expression -> expression BOOLEQUAL expression','expression',3,'p_expression_relop','parse.py',140),
  ('expression -> expression AND expression','expression',3,'p_expression_logical','parse.py',156),
  ('expression -> expression OR expression','expression',3,'p_expression_logical','parse.py',157),
  ('expression -> ID INCREMENT','expression',2,'p_expression_increment','parse.py',165),
  ('expression -> ID DECREMENT','expression',2,'p_expression_decrement','parse.py',169),
  ('assignment -> ID INCREMENT STMT_TERMINATOR','assignment',3,'p_assignment_increment','parse.py',174),
  ('assignment -> ID DECREMENT STMT_TERMINATOR','assignment',3,'p_assignment_decrement','parse.py',178),
  ('expression -> expression ARROW ID','expression',3,'p_expression_arrow','parse.py',183),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE code RBRACE','if_statement',7,'p_if_statement','parse.py',188),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE code RBRACE ELSE LBRACE code RBRACE','if_statement',11,'p_if_statement','parse.py',189),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE code RBRACE','while_statement',7,'p_while_statement','parse.py',196),
  ('for_statement -> FOR LPAREN assignment STMT_TERMINATOR expression STMT_TERMINATOR expression RPAREN LBRACE code RBRACE','for_statement',11,'p_for_statement','parse.py',200),
  ('arguments -> expression','arguments',1,'p_arguments','parse.py',204),
  ('arguments -> arguments COMMA expression','arguments',3,'p_arguments','parse.py',205),
  ('arguments -> empty','arguments',1,'p_arguments','parse.py',206),
  ('array_declaration -> datatype ID LBRACKET INTCONST RBRACKET','array_declaration',5,'p_array_declaration','parse.py',216),
  ('array_assignment -> ID LBRACKET expression RBRACKET EQUAL expression','array_assignment',6,'p_array_assignment','parse.py',221),
  ('array_access -> ID LBRACKET expression RBRACKET','array_access',4,'p_array_access','parse.py',226),
  ('write_statement -> WRITE LPAREN expression RPAREN STMT_TERMINATOR','write_statement',5,'p_write_statement','parse.py',231),
  ('writeln_statement -> WRITELN LPAREN expression RPAREN STMT_TERMINATOR','writeln_statement',5,'p_writeln_statement','parse.py',235),
  ('break_statement -> BREAK STMT_TERMINATOR','break_statement',2,'p_break_statement','parse.py',239),
  ('return_statement -> RETURN expression STMT_TERMINATOR','return_statement',3,'p_return_statement','parse.py',243),
  ('return_statement -> RETURN STMT_TERMINATOR','return_statement',2,'p_return_statement','parse.py',244),
  ('empty -> <empty>','empty',0,'p_empty','parse.py',251),
]