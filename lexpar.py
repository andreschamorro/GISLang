import gisclass

tokens = [
        'NAME', 'NUMBER', 
        'EQUALS', 'PLUS', 'MINUS',
        'LPAREN', 'RPAREN', 'COMMA', 
        ]

reserved = {
        'quit': 'QUIT',
        'for' : 'FOR', 
        'in'  : 'IN',
        'Point' : 'POINT', 
        'Line'  : 'LINE', 
        'Edification' : 'EDIFICATION',
        'House' : 'HOUSE',
        'School' : 'SCHOOL',
        'Hospital' : 'HOSPITAL',
        'Commercial' : 'COMMERCIAL', 
        'Region' : 'REGION',
        'Block' : 'BLOCK',
        'Neighborhood' : 'NEIGHBORHOOD',
        'Town' : 'TOWN',
        'State' : 'STATE',
        'River' : 'RIVER',
        'Lake' : 'LAKE',
        }

tokens += list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_COMMA   = r'\,'
# Ignored characters
t_ignore = " \t"

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

def t_NUMBER(t):
    r'\d+(\.\d{1,2})?'    
    t.value = float(t.value)
    return t

def t_POINT(t):
    r'\([-|+]?[0-9]+(\.[0-9][0-9]?)?\,[-|+]?[0-9]+(\.[0-9][0-9]?)?\)'
    v = eval(t.value)
    t.value = gisclass.Point(v[0], v[1])       
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal Character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    )

# dictionary of names
names = { }

def p_statement_assign(p):
    'statement : NAME EQUALS expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print(p[1])

def p_expression_edification(p):
    '''expression : EDIFICATION
                  | EDIFICATION POINT'''
    if len(p) == 2:
        p[0] = gisclass.Edification()
    elif len(p) == 3:
        p[0] = gisclass.Edification(p[2])

def p_expression_house(p):
    '''expression : HOUSE
                  | HOUSE POINT'''
    if len(p) == 2:
        p[0] = gisclass.House()
    elif len(p) == 3:
        p[0] = gisclass.House(p[2])

def p_expression_hospital(p):
    '''expression : HOSPITAL
                  | HOSPITAL POINT'''
    if len(p) == 2:
        p[0] = gisclass.Hospital()
    elif len(p) == 3:
        p[0] = gisclass.Hospital(p[2])

def p_expression_commercial(p):
    '''expression : COMMERCIAL
                  | COMMERCIAL POINT'''
    if len(p) == 2:
        p[0] = gisclass.Commercial()
    elif len(p) == 3:
        p[0] = gisclass.Commercial(p[2])

def p_expression_school(p):
    '''expression : SCHOOL
                  | SCHOOL POINT'''
    if len(p) == 2:
        p[0] = gisclass.School()
    elif len(p) == 3:
        p[0] = gisclass.School(p[2])

def p_expression_region(p):
    '''expression : REGION
                  | REGION POINT
                  | REGION LPAREN NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.Region()
    elif len(p) == 3:
        p[0] = gisclass.Region([p[2]])
    elif len(p) == 5:
        p[0] = gisclass.Region([p[3]])

def p_expression_block(p):
    '''expression : BLOCK
                  | BLOCK LPAREN expression COMMA expression RPAREN
                  | BLOCK LPAREN NAME COMMA NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.Block()
    elif len(p) == 7:
        p[0] = gisclass.Block(p[3], p[5])

def p_expression_neighborhood(p):
    '''expression : NEIGHBORHOOD
                  | NEIGHBORHOOD LPAREN expression COMMA expression RPAREN
                  | NEIGHBORHOOD LPAREN NAME COMMA NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.Neighborhood()
    elif len(p) == 3:
        p[0] = gisclass.Neighborhood(p[3], p[5])

def p_expression_Town(p):
    '''expression : TOWN
                  | TOWN LPAREN expression COMMA expression RPAREN
                  | TOWN LPAREN NAME COMMA NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.Town()
    elif len(p) == 3:
        p[0] = gisclass.Town(p[3], p[5])

def p_expression_state(p):
    '''expression : STATE
                  | STATE LPAREN expression COMMA expression RPAREN
                  | STATE LPAREN NAME COMMA NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.State()
    elif len(p) == 3:
        p[0] = gisclass.State(p[3], p[5])

def p_expression_lake(p):
    '''expression : LAKE 
                  | LAKE POINT
                  | LAKE LPAREN NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.Lake()
    elif len(p) == 3:
        p[0] = gisclass.Lake([p[2]])
    elif len(p) == 5:
        p[0] = gisclass.Lake([p[3]])

def p_expression_river(p):
    '''expression : RIVER
                  | RIVER LPAREN expression COMMA expression RPAREN
                  | RIVER LPAREN NAME COMMA NAME RPAREN '''
    if len(p) == 2:
        p[0] = gisclass.State()
    elif len(p) == 3:
        p[0] = gisclass.State(p[3], p[5])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression'''
    if p[2] == '+'   : p[0] = p[1] + p[3] 
    elif p[2] == '-' : p[0] = p[1] - p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'    
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_point(p):
    'expression : POINT'
    p[0] = p[1]

def p_expression_line(p):
    'expression : LINE POINT'
    p[0] = gisclass.Line([p[2]])

def p_expression_name(p):
    'expression : NAME'
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_quit(p):
    'expression : QUIT'
    p[0] = quit()
        
def p_error(p):
    print("Syntax error at '%s'" % p.value)

import ply.yacc as yacc

yacc.yacc()

#Desacomentar esta parte y comentar la seccion de codigo de abajo
#para utilizar el modo interactivo

while True:
    try:
        s = raw_input('gis >> ')   # use input() on Python 3
    except EOFError:
        break
    yacc.parse(s)
