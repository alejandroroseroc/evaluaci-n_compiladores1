grammar IfElseLang;

program   : statement+ EOF ;
statement : assignment | ifStatement ;

assignment : ID ASSIGN expr SEMI ;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE
      (ELSE LBRACE statement* RBRACE)?
    ;

condition : expr operator expr ;
expr      : ID | NUMBER ;
operator  : GT | LT | EQ | GE | LE | NE ;

IF     : 'if' ;
ELSE   : 'else' ;
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
SEMI   : ';' ;

// Colocamos 'EQ' antes de 'ASSIGN' por claridad (aunque '==' gana por ser más largo)
EQ     : '==' ;
GE     : '>=' ;
LE     : '<=' ;
NE     : '!=' ;
GT     : '>' ;
LT     : '<' ;
ASSIGN : '=' ;

// Identificadores, números y espacios
ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER : [0-9]+ ;
WS     : [ \t\r\n]+ -> skip ;
