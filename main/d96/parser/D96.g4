// Huỳnh Bảo Minh -2020047

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decls EOF ;

decls: class_decl decls|class_decl;
class_decl:CLASS (ID | ID COLON ID) LCB (class_bodys|) RCB;
class_bodys:class_body class_bodys|class_body;
class_body:attribute_decl|method_decl;


variable_decl:VAR list_name COLON typ_var (SET list_exp|) SEMI;

const_decl:VAL list_name COLON typ_var (SET list_exp|) SEMI;
//Attribute declaration

typ_name :VAL | VAR;

attribute_decl: variable_decl|const_decl ;

list_name:(ID | Dollar_id) COMMA  list_name| (ID | Dollar_id);

name_att: ID | Dollar_id;

// optionally: SET list_exp|;

list_exp:(expr|NULL) COMMA list_exp |(expr|NULL) ;

//Method declaration
method_decl: constructor|destructor|(ID | Dollar_id) LP (parameter|) RP block_stm ;

parameter: identifer_list COLON typ_var SEMI parameter|identifer_list COLON typ_var;

identifer_list: name_att COMMA identifer_list| name_att;

constructor:CONSTRUCTOR LP (parameter|) RP block_stm;

destructor:DESTRUCTOR LP  RP block_stm;

//STATEMENTS
// variable_decl:typ_name list_name COLON typ_var optionally SEMI ;

block_stm:LCB  (statements|) RCB ;

statement: variable_decl|assignment_statement| if_statement|foreach_stmt|break_stmt|cont_stmt|call_stmt |return_stmt|block_stm|member_access;

statements: statement statements|statement;

//index operators

index_operators : LSB expr RSB index_operators| LSB expr RSB ;

//Method call
func_call: expr DOT name_att LP (parameter | ) RP;


//Expression
expr: expr1 (AD|ED) expr1 | expr1;
expr1: expr2 (EQ|NE|LT|GT|LTE|GTE) expr2 |expr2;
expr2: expr2 (AND|OR) expr3| expr3;
expr3: expr3 (ADD|SUB) expr4 | expr4;
expr4: expr4 (MUL|DIV|MOD) expr5| expr5;
expr5: NOT expr5 |expr6;
expr6: SUB expr6 |expr7;
expr7: expr7 index_operators|expr8;
expr8: expr8 DOT ID |expr8 DOT ID LP (list_exp|) RP |expr9;
expr9: ID ACCESS Dollar_id|ID ACCESS Dollar_id LP (list_exp|) RP|expr10;
expr10: NEW ID LP (list_exp|) RP |expr11;
expr11: LP expr RP |operand ;
operand:SELF| NULL| name_att | literal;
literal:INTLIT|FLOATLIT|boolit|STRINGLIT|arraylit;
TRUE:'True';             
FALSE:'False'; 
BREAK:'Break';          
CONTINUE:'Continue';     
IF:'If';

ELSEIF:'Elseif';       
ELSE:'Else';                 
FOREACH:'Foreach';

             
ARRAY:'Array';

INT:'Int';                
FLOAT:'Float';              
BOOLEAN:'Boolean';

STRING:'String';       
NULL:'Null';					
BY:'By';

CLASS: 'Class';			
VAL:'Val';					
VAR:'Var';

NEW:'New';				
RETURN:'Return';			
IN:'In';
CONSTRUCTOR:'Constructor';		
DESTRUCTOR:'Destructor';
SELF : 'Self' ;

instance_method:expr DOT ID LP (list_exp|) RP;
static_method:ID ACCESS Dollar_id LP (list_exp|) RP;
member_access:instance_method SEMI| static_method SEMI;

//ASSIGNMENT STATEMENT

assignment_statement: expr SET expr SEMI;


//IF-STATEMENT

if_statement: IF LP expr RP block_stm (elseStmt|);

elseStmt:elif_stm elseStmt| elif_stm|else_stm;

elif_stm: ELSEIF LP expr RP block_stm;

else_stm: ELSE block_stm ;

//FOREACH-STATEMENT
DDOTS:'..';

foreach_stmt: FOREACH LP ID IN INTLIT DDOTS INTLIT (BY INTLIT)? RP block_stm;

//Break-statemt

break_stmt: BREAK SEMI;

//Continue statement

cont_stmt: CONTINUE SEMI;

//Return statement

call_stmt: func_call SEMI;

return_stmt: RETURN (expr| ) SEMI;

//TYPE
typ_var: INT| FLOAT|BOOLEAN|STRING|array|class_type;
class_type:ID;
array: ARRAY LSB typ_var COMMA INTLIT RSB;

//Skip
WS : [ \t\r\n\f]+ -> skip ; 

//COMMENT
COMMENT: '##' .*? '##' -> skip ;

//OPERATOR
ADD:'+';    
SUB:'-';    
MUL:'*';    
DIV:'/';

MOD:'%';    NOT:'!';    AND:'&&';   OR:'||';

EQ:'==';    SET:'=';    NE:'!=';    GT:'>';

GTE:'>=';   LT:'<';     LTE:'<=';   ED:'==.';

AD:'+.';

//Seperators
LP: '(';        RP: ')';        LSB: '[';       RSB: ']'; 
COLON: ':';     DOT: '.';       COMMA: ',';     SEMI: ';';
LCB: '{';       RCB: '}'; 		ACCESS:'::';




///////////////////////LITERALS////////////////////////
//Integer
INTLIT: (DEC|HEX|OCT|BIN)
    {
        string = str(self.text)
        self.text = string.replace("_","")     
    };

fragment DEC:[1-9][0-9_]*|'0';

fragment HEX:'0' [xX] ([0-9A-F])+;

fragment OCT:'0' ([0-7])+;

fragment BIN:'0' [bB] ([01])+ ;

//BOOLEN
boolit: TRUE|FALSE;

//FLOATLIT
fragment IP:DEC;

fragment DP:DOT (IP|[0-9]*)?;

fragment EP:[eE] (ADD|SUB)? IP;

FLOATLIT:(IP DP EP      //example: 190.203e13
        |DP EP          //example:  .123E-10
        |IP EP          //example:  24E200
        |IP DP)         //example:  2.3
        {
            string = str(self.text)
            self.text = string.replace("_","")   
        };




//STRINGLIT
STRINGLIT: DoubQ STR_CHAR* DoubQ
	{
		y = str(self.text)
		self.text = y[1:-1]         
		                           
	};

//ARRAYLIT
//INDEXED ARAAY     Array(1, 5, 7, 12),Array("Kangxi", "Yongzheng", "Qianlong"),..
arraylit:iar|mar;

iar:ARRAY LP (aints|afloats|astrings|asbools|) RP;

aints: INTLIT COMMA aints | INTLIT;

afloats: FLOATLIT COMMA afloats | FLOATLIT;

astrings: STRINGLIT COMMA astrings | STRINGLIT;

asbools: boolit COMMA asbools | boolit;

//MULTI-DIMENSTION ARRAYS   Các array lồng nhau

//      Array (
//          Array("Volvo", "22", "18"),
//          Array("Saab", "5", "2"),
//          Array("Land Rover", "17", "15")
//          )


marraylists: iar COMMA marraylists| iar;     // có thể có 1 hoặc nhiều array.
mar:ARRAY LP marraylists RP;
ID: [a-zA-Z_] [a-zA-Z_0-9]*; 

Dollar_id:'$'[a-zA-Z0-9_]+;

fragment DoubQ:'"';

fragment SignQ:'\'';

fragment STR_CHAR: ~[\b\t\n\f\r'"\\]|SignQ DoubQ |ESC_SEQ ;     // bỏ "

fragment ESC_SEQ: '\\' [btnfr'"\\] ;    // bỏ "
//ERROR
ERROR_TOKEN:.{raise ErrorToken(self.text)};

UNCLOSE_STRING: '"' STR_CHAR* ( [\b\t\n\f\r"'\\] | EOF )
	{
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~[\\] ;

UNTERMINATED_COMMENT: '##' .*? ~'#' ~'#';

//KEYWORK
fragment A: [aA];   
fragment B: [bB];   
fragment C: [cC];
fragment D: [dD];   
fragment E: [eE];   
fragment F: [fF];
fragment G: [gG];   
fragment H: [hH];   
fragment I: [iI];
fragment J: [jJ];   
fragment K: [kK];   
fragment L: [lL];
fragment M: [mM];   
fragment N: [nN];   
fragment O: [oO];
fragment P: [pP];   
fragment Q: [qQ];   
fragment R: [rR];
fragment S: [sS];   
fragment T: [tT];   
fragment U: [uU];
fragment V: [vV];   
fragment W: [wW];   
fragment X: [xX];
fragment Y: [yY];   
fragment Z: [zZ];
