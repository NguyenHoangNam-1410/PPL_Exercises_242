grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl_stmt | funcdecl)+ EOF;

vardecl_stmt: data_type ID (',' ID)* ';';

funcdecl: data_type ID '(' param (';' param)* ')' '{' statement* '}';

param: data_type ID ((',') ID)* ;

statement: vardecl_stmt | assign | return_stmt | func_call;

func_call: ID '(' expr (',' expr)* ')' ';';

return_stmt: 'return' expr ';';

assign: ID '=' expr ';';

data_type: 'int' | 'float';

expr
    : expr '+' expr      
    | expr '-' expr      
    | expr '*' expr      
    | expr '/' expr      
    | '(' expr ')'       
    | INT                
    | FLOAT              
    | ID                 
    | ID '(' (expr (',' expr)*)? ')'
    ;

ID: [a-zA-Z]+;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: . {raise ErrorToken(self.text)};
