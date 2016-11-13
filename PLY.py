
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

from gisclass import *
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS',
    'LPAREN','RPAREN', 'TYPE', 'COMMA', 'TYPEOF', 'FOR', 'IN',
    )

# Tokens

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA   = r'\,'
t_IN      = r'in'

def t_FOR(t):
    r'for'
    return t

def t_TYPEOF(t):
    r'type'
    return t

def t_TYPE(t):
    r'House|Edification|Hospital|Commercial|School|Street'
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]
#pora ahora empty object
def p_expression_for(t):
    'expression : FOR NAME IN NAME'
    var = names[t[2]]
    toIter = names[t[4]]
    #for var in toIter.elements(var.key):
        
        
def p_expression_emptyO(t):
    'expression : TYPE NAME'    
    names[t[2]] = House()
def p_expression_typeof(t):
    'expression : TYPEOF LPAREN NAME RPAREN'
    print(names[t[3]].key)
def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]
def p_expression_type(p):
    'expression : TYPE NAME EQUALS LPAREN NUMBER COMMA NUMBER RPAREN'
    if p[1] == 'Edification':
        try:
            names[p[2]]=Edification(p[5],p[7]);
            
        except:
            print("Undefined type '%s'" % p[1])
            
    elif p[1] == 'House':
        try:
            names[p[2]]=House(p[5],p[7]);
        except:
            print("Undefined type '%s'" % p[1])
    elif p[1] == 'School':
        try:
            names[p[2]]=School(p[5],p[7]);
        except:
            print("Undefined type '%s'" % p[1])
    elif p[1] == 'Hospital':
        try:
            names[p[2]]=Hospital(p[5],p[7]);
        except:
            print("Undefined type '%s'" % p[1])
    elif p[1] == 'Commercial':
        try:
            names[p[2]]=Commercial(p[5],p[7]);
        except:
            print("Undefined type '%s'" % p[1])
    elif p[1] == 'Street':
        try:
            names[p[2]]=Sreet(p[5],p[7]);
        except:
            print("Undefined type '%s'" % p[1])
    else:
        print("Not a type");



def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
