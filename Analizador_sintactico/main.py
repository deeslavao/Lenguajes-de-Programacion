from Lexico import lexico
from prediccion import get_prediccion
prediccion,primeros,siguientes = get_prediccion()
def emparejar(letra):
    global token 
    if token.lexema == letra: 
        token = getNextToken()
    else:
        errorSintaxis(letra)
def getNextToken():
    if len(tokenLexico) == 0:
        token.lexema = "$"
        return token
    else: return tokenLexico.pop(0)
def errorSintaxis(regla): 
    print(f"se encontro {regla}")
    exit()
def INICIO(): 
    if  token.lexema == 'programa' or token.lexema == 'var' or token.lexema == 'const' or token.lexema == 'tipos' or token.lexema == 'inicio' : 
        PROG()
        ESPECIFICACION()
        emparejar('inicio')
        SENTENCIAS()
        emparejar('fin')
        SUBRUTINAS()
    else: errorSintaxis('INICIO')
def PROG(): 
    if  token.lexema == 'programa' : 
        emparejar('programa')
        emparejar('id')
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('PROG')
def ESPECIFICACION(): 
    if  token.lexema == 'var' : 
        emparejar('var')
        VAR()
        ESPECIFICACION()
    elif token.lexema == 'const' : 
        emparejar('const')
        CONST()
        ESPECIFICACION()
    elif token.lexema == 'tipos' : 
        emparejar('tipos')
        TIPOS()
        ESPECIFICACION()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('ESPECIFICACION')
def VAR(): 
    if  token.lexema == 'id' or token.lexema == 'tk_dos_puntos' : 
        ID()
        emparejar('tk_dos_puntos')
        RMT()
        VAR()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('VAR')
def ID(): 
    if  token.lexema == 'id' : 
        emparejar('id')
        ID2()
    else: errorSintaxis('ID')
def ID2(): 
    if  token.lexema == 'tk_coma' : 
        emparejar('tk_coma')
        ID()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('ID2')
def CONST(): 
    if  token.lexema == 'id' : 
        emparejar('id')
        emparejar('tk_asignacion')
        CONST2()
        CONST()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('CONST')
def CONST2(): 
    if  token.lexema == 'tk_numero' : 
        emparejar('tk_numero')
    elif token.lexema == 'tk_cadena' : 
        emparejar('tk_cadena')
    elif token.lexema == 'TRUE' : 
        emparejar('TRUE')
    elif token.lexema == 'FALSE' : 
        emparejar('FALSE')
    elif token.lexema == 'SI' : 
        emparejar('SI')
    elif token.lexema == 'NO' : 
        emparejar('NO')
    else: errorSintaxis('CONST2')
def RMT(): 
    if  token.lexema == 'numerico' or token.lexema == 'cadena' or token.lexema == 'logico' : 
        TIPODATO()
    elif token.lexema == 'vector' : 
        emparejar('vector')
        emparejar('tk_corchete_izquierdo')
        emparejar('tk_numero')
        emparejar('tk_corchete_derecho')
        TIPODATO()
    elif token.lexema == 'matriz' : 
        emparejar('matriz')
        emparejar('tk_corchete_izquierdo')
        emparejar('tk_numero')
        emparejar('tk_coma')
        emparejar('tk_numero')
        emparejar('tk_corchete_derecho')
        TIPODATO()
    elif token.lexema == 'registro' : 
        emparejar('registro')
        REGISTRO()
    else: errorSintaxis('RMT')
def TIPODATO(): 
    if  token.lexema == 'numerico' : 
        emparejar('numerico')
    elif token.lexema == 'cadena' : 
        emparejar('cadena')
    elif token.lexema == 'logico' : 
        emparejar('logico')
    else: errorSintaxis('TIPODATO')
def REGISTRO(): 
    if  token.lexema == 'tk_llave_izquierda' : 
        emparejar('tk_llave_izquierda')
        VAR()
        emparejar('tk_llave_derecha')
    else: errorSintaxis('REGISTRO')
def TIPOS(): 
    if  token.lexema == 'id' : 
        emparejar('id')
        emparejar('tk_dos_puntos')
        RMT()
        TIPOS()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('TIPOS')
def SENTENCIAS(): 
    if  token.lexema == 'id' : 
        emparejar('id')
        emparejar('tk_dos_puntos')
        EXPRE()
        SENTENCIAS()
    elif token.lexema == 'si' : 
        emparejar('si')
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
        emparejar('tk_llave_izquierda')
        SENTENCIAS()
        ELSE()
        emparejar('tk_llave_derecha')
        SENTENCIAS()
    elif token.lexema == 'mientras' : 
        emparejar('mientras')
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
        emparejar('tk_llave_izquierda')
        SENTENCIAS()
        emparejar('tk_parentesis_derecho')
        SENTENCIAS()
    elif token.lexema == 'repetir' : 
        emparejar('repetir')
        SENTENCIAS()
        emparejar('hasta')
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
        SENTENCIAS()
    elif token.lexema == 'eval' : 
        emparejar('eval')
        emparejar('tk_llave_izquierda')
        CASO()
        emparejar('sino')
        SENTENCIAS()
        emparejar('tk_llave_derecha')
        SENTENCIAS()
    elif token.lexema == 'desde' : 
        emparejar('desde')
        emparejar('id')
        emparejar('tk_asignacion')
        EXPRE()
        emparejar('hasta')
        EXPRE()
        INCREMENTO()
        emparejar('tk_llave_izquierda')
        SENTENCIAS()
        emparejar('tk_llave_derecha')
        SENTENCIAS()
    elif token.lexema == 'id' : 
        emparejar('id')
        emparejar('tk_dos_puntos')
        EXPRE()
        SENTENCIAS()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('SENTENCIAS')
def EXPRE(): 
    if  token.lexema == 'tk_mayor' or token.lexema == 'tk_mayor_igual' or token.lexema == 'tk_menor' or token.lexema == 'tk_menor_igual' or token.lexema == 'tk_igual_que' or token.lexema == 'tk_suma' or token.lexema == 'tk_resta' or token.lexema == 'tk_potenciacion' or token.lexema == 'tk_modulo' or token.lexema == 'tk_division' or token.lexema == 'tk_mayor' or token.lexema == 'tk_mayor_igual' or token.lexema == 'tk_menor' or token.lexema == 'tk_menor_igual' or token.lexema == 'tk_igual_que' or token.lexema == 'tk_suma' or token.lexema == 'tk_resta' or token.lexema == 'tk_potenciacion' or token.lexema == 'tk_modulo' or token.lexema == 'tk_division' or token.lexema == 'tk_mayor' or token.lexema == 'tk_mayor_igual' or token.lexema == 'tk_menor' or token.lexema == 'tk_menor_igual' or token.lexema == 'tk_igual_que' or token.lexema == 'tk_suma' or token.lexema == 'tk_resta' or token.lexema == 'tk_potenciacion' or token.lexema == 'tk_modulo' or token.lexema == 'tk_division' or token.lexema == 'and' or token.lexema == 'or' : 
        EXPRE()
        OPER()
        EXPRE()
        AND()
    elif token.lexema == 'tk_parentesis_izquierdo' : 
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
    elif token.lexema == 'tk_numero' : 
        emparejar('tk_numero')
    elif token.lexema == 'tk_cadena' : 
        emparejar('tk_cadena')
    elif token.lexema == 'id' : 
        emparejar('id')
    else: errorSintaxis('EXPRE')
def AND(): 
    if  token.lexema == 'and' : 
        emparejar('and')
        EXPRE()
    elif token.lexema == 'or' : 
        emparejar('or')
        EXPRE()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('AND')
def OPER(): 
    if  token.lexema == 'tk_mayor' : 
        emparejar('tk_mayor')
    elif token.lexema == 'tk_mayor_igual' : 
        emparejar('tk_mayor_igual')
    elif token.lexema == 'tk_menor' : 
        emparejar('tk_menor')
    elif token.lexema == 'tk_menor_igual' : 
        emparejar('tk_menor_igual')
    elif token.lexema == 'tk_igual_que' : 
        emparejar('tk_igual_que')
    elif token.lexema == 'tk_suma' : 
        emparejar('tk_suma')
    elif token.lexema == 'tk_resta' : 
        emparejar('tk_resta')
    elif token.lexema == 'tk_potenciacion' : 
        emparejar('tk_potenciacion')
    elif token.lexema == 'tk_modulo' : 
        emparejar('tk_modulo')
    elif token.lexema == 'tk_division' : 
        emparejar('tk_division')
    else: errorSintaxis('OPER')
def ELSE(): 
    if  token.lexema == 'sino' : 
        emparejar('sino')
        SENTENCIAS()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('ELSE')
def CASO(): 
    if  token.lexema == 'caso' : 
        emparejar('caso')
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
        SENTENCIAS()
        CASO()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('CASO')
def INCREMENTO(): 
    if  token.lexema == 'paso' : 
        emparejar('paso')
        EXPRE()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('INCREMENTO')
def ARGUMENTOS(): 
    if  token.lexema == 'tk_numero' : 
        emparejar('tk_numero')
        ARGUMENTOS2()
    elif token.lexema == 'tk_cadena' : 
        emparejar('tk_cadena')
        ARGUMENTOS2()
    elif token.lexema == 'id' : 
        emparejar('id')
        ARGUMENTOS2()
    else: errorSintaxis('ARGUMENTOS')
def ARGUMENTOS2(): 
    if  token.lexema == 'tk_coma' : 
        emparejar('tk_coma')
        ARGUMENTOS()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('ARGUMENTOS2')
def SUBRUTINAS(): 
    if  token.lexema == 'subrutina' : 
        emparejar('subrutina')
        emparejar('id')
        emparejar('tk_parentesis_izquierdo')
        REF()
        EXPRESUB()
        emparejar('tk_parentesis_derecho')
        VALOREF()
        SUBRUTINAS()
    else: errorSintaxis('SUBRUTINAS')
def REF(): 
    if  token.lexema == 'ref' : 
        emparejar('ref')
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('REF')
def EXPRESUB(): 
    if  token.lexema == 'tk_dos_puntos' : 
        ID()
        emparejar('tk_dos_puntos')
        TIPODATO()
        EXPRESUB2()
    else: errorSintaxis('EXPRESUB')
def EXPRESUB2(): 
    if  token.lexema == 'tk_punto_y_coma' : 
        emparejar('tk_punto_y_coma')
        EXPRESUB()
    elif token.lexema == 'epsilon' : 
        pass 
    else: errorSintaxis('EXPRESUB2')
def VALOREF(): 
    if  token.lexema == 'retorna' : 
        emparejar('retorna')
        TIPODATO()
        ESPECIFICACION()
        emparejar('inicio')
        SENTENCIAS()
        emparejar('retorna')
        emparejar('tk_parentesis_izquierdo')
        EXPRE()
        emparejar('tk_parentesis_derecho')
        emparejar('fin')
    elif token.lexema == 'inicio' : 
        ESPECIFICACION()
        emparejar('inicio')
        SENTENCIAS()
        emparejar('fin')
    else: errorSintaxis('VALOREF')
tokenLexico = lexico()
token = getNextToken()
INICIO()
if token.lexema != '$':
    print('Error sintactico: falta inicio')
    exit()

print('El analisis sintactico ha finalizado exitosamente.')