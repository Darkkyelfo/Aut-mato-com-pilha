'''
Created on 22 de ago de 2016

@author: Raul
'''
import ply.lex as lex

# List of token names.   This is always required
tokens = (
    #tipos
   'NUMBER',
   'STRING',
   #sinais
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'IGUAL',
   'ATRIBUICAO',
   'MAIORQUE',
   'MENORQUE',
   
   'LPAREN',
   'RPAREN',
   'IDENTIFICADOR',
   'CHAVESD',
   'CHAVESE',
   'COMENTARIOS',
   #palavras reservadas
   'IF',
   'ELSE',
   'WHILE',
   'FOR',

)
RESERVADA = {'if':'IF','else':'ELSE','while':'WHILE','for':'FOR'}
# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_IGUAL = r'=='
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ATRIBUICAO = r'='
t_MAIORQUE = r'>'
t_MENORQUE = r'<'
t_CHAVESE = r'{'
t_CHAVESD = r'}'
t_STRING = r'\"(\d|\D)*\"'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'(\d+.\d+)|(\d+)'
    if('.' in t.value):
        t.value = float(t.value)
    else:
        t.value = int(t.value)     
    return t

def t_IDENTIFICADOR(t):
    r'([A-Z]|[a-z])+([0-9]|([A-Z]|[a-z]))*' 
    if t.value in RESERVADA:
        t.type = RESERVADA[t.value]
    return t
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMENTARIOS(t):
    r'\#(\w|\s)*\n'
    pass
    
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
lexer.input("""x55555h=2.576
while(x>3){
    #isso é um comentario
    if(x>   5){
        print("oi")
    }
}
""")

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)