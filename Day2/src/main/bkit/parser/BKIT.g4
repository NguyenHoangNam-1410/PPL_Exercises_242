grammar BKIT;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

fragment Letter: [a-z] ;
fragment Digit: [0-9] ;

//ID: Letter (Letter | Digit)* ;

/*fragment Float1: '.'Digit+ ;
fragment Float2: '.'Digit* ;
fragment Expo: [eE][+-]? Digit+ ;
REAL: (Digit+ Float1? Expo?) | (Float1 Expo?) |  (Digit+ '.' Expo?);*/

//STRING: '\'' ( '\'' '\'' | ~'\'' )* '\'' ;

/*fragment Two_Digit : [1-9] Digit ;
fragment Three_Digit : '1' Digit Digit | '2' [0-4] Digit | '25' [0-5] ;
fragment Octet : '0' | Digit | Two_Digit | Three_Digit ;
IPv4_ADDRESS : Octet '.' Octet '.' Octet '.' Octet ;*/

Php_int: '0' | [1-9] (Digit | '_' Digit)* {self.text=self.text.replace('_', '')};

SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .  {raise ErrorToken(self.text)};
