grammar WhileLang;

program: statement+ EOF;

statement: assignment 
         | whileStatement 
         | ifStatement 
         | breakStatement 
         | continueStatement;

assignment: ID ASSIGN expr SEMI;

whileStatement: WHILE LPAREN condition RPAREN LBRACE statement* RBRACE;

ifStatement: IF LPAREN condition RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)?;

breakStatement: BREAK SEMI;

continueStatement: CONTINUE SEMI;

condition: expr operator expr;

expr: expr (PLUS | MINUS | MULT | DIV) expr
    | ID
    | NUMBER;

operator: GT | LT | EQ | NE;

WHILE: 'while';
IF: 'if';
ELSE: 'else';
BREAK: 'break';
CONTINUE: 'continue';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
GT: '>';
LT: '<';
EQ: '==';
NE: '!=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
WS: [ \t\r\n]+ -> skip;
