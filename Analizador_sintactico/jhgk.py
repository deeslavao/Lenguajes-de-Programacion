import Lexico
from prediccion import get_prediccion

prediccion,primeros,siguientes = get_prediccion()
def emparejar(letra): 
	if token == letra: 
		token = getNextToken()
	else:
		errorSintaxis(letra)
def getNextToken(): 
	
	return tokenLexico.pop(0)
def errorSintaxis(regla): 
	return prediccion[regla]
def INICIO(): 
 	if  token == 'programa' or token == 'var' or token == 'const' or token == 'tipos' or token == 'inicio' : 
		PROG()
		ESPECIFICACION()
		emparejar('inicio')
		SENTENCIAS()
		emparejar('fin')
		SUBRUTINAS()
	else: errorSintaxis('INICIO')
def PROG(): 
 	if  token == 'programa' : 
		emparejar('programa')
		emparejar('id')
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('PROG')
def ESPECIFICACION(): 
 	if  token == 'var' : 
		emparejar('var')
		VAR()
		ESPECIFICACION()
	elif token == 'const' : 
		emparejar('const')
		CONST()
		ESPECIFICACION()
	elif token == 'tipos' : 
		emparejar('tipos')
		TIPOS()
		ESPECIFICACION()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('ESPECIFICACION')
def VAR(): 
 	if  token == 'id' or token == 'tk_dos_puntos' : 
		ID()
		emparejar('tk_dos_puntos')
		RMT()
		VAR()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('VAR')
def ID(): 
 	if  token == 'id' : 
		emparejar('id')
		ID2()
	else: errorSintaxis('ID')
def ID2(): 
 	if  token == 'tk_coma' : 
		emparejar('tk_coma')
		ID()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('ID2')
def CONST(): 
 	if  token == 'id' : 
		emparejar('id')
		emparejar('tk_asignacion')
		CONST2()
		CONST()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('CONST')
def CONST2(): 
 	if  token == 'tk_numero' : 
		emparejar('tk_numero')
	elif token == 'tk_cadena' : 
		emparejar('tk_cadena')
	elif token == 'TRUE' : 
		emparejar('TRUE')
	elif token == 'FALSE' : 
		emparejar('FALSE')
	elif token == 'SI' : 
		emparejar('SI')
	elif token == 'NO' : 
		emparejar('NO')
	else: errorSintaxis('CONST2')
def RMT(): 
 	if  token == 'numerico' or token == 'cadena' or token == 'logico' : 
		TIPODATO()
	elif token == 'vector' : 
		emparejar('vector')
		emparejar('tk_corchete_izquierdo')
		emparejar('tk_numero')
		emparejar('tk_corchete_derecho')
		TIPODATO()
	elif token == 'matriz' : 
		emparejar('matriz')
		emparejar('tk_corchete_izquierdo')
		emparejar('tk_numero')
		emparejar('tk_coma')
		emparejar('tk_numero')
		emparejar('tk_corchete_derecho')
		TIPODATO()
	elif token == 'registro' : 
		emparejar('registro')
		REGISTRO()
	else: errorSintaxis('RMT')
def TIPODATO(): 
 	if  token == 'numerico' : 
		emparejar('numerico')
	elif token == 'cadena' : 
		emparejar('cadena')
	elif token == 'logico' : 
		emparejar('logico')
	else: errorSintaxis('TIPODATO')
def REGISTRO(): 
 	if  token == 'tk_llave_izquierda' : 
		emparejar('tk_llave_izquierda')
		VAR()
		emparejar('tk_llave_derecha')
	else: errorSintaxis('REGISTRO')
def TIPOS(): 
 	if  token == 'id' : 
		emparejar('id')
		emparejar('tk_dos_puntos')
		RMT()
		TIPOS()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('TIPOS')
def SENTENCIAS(): 
 	if  token == 'id' : 
		emparejar('id')
		emparejar('tk_dos_puntos')
		EXPRE()
		SENTENCIAS()
	elif token == 'si' : 
		emparejar('si')
		emparejar('tk_parentesis_izquierdo')
		EXPRE()
		emparejar('tk_parentesis_derecho')
		emparejar('tk_llave_izquierda')
		SENTENCIAS()
		ELSE()
		emparejar('tk_llave_derecha')
		SENTENCIAS()
	elif token == 'mientras' : 
		emparejar('mientras')
		emparejar('tk_parentesis_izquierdo')
		EXPRE()
		emparejar('tk_parentesis_derecho')
		emparejar('tk_llave_izquierda')
		SENTENCIAS()
		emparejar('tk_parentesis_derecho')
		SENTENCIAS()
	elif token == 'repetir' : 
		emparejar('repetir')
		SENTENCIAS()
		emparejar('hasta')
		emparejar('tk_parentesis_izquierdo')
		EXPRE()
		emparejar('tk_parentesis_derecho')
		SENTENCIAS()
	elif token == 'eval' : 
		emparejar('eval')
		emparejar('tk_llave_izquierda')
		CASO()
		emparejar('sino')
		SENTENCIAS()
		emparejar('tk_llave_derecha')
		SENTENCIAS()
	elif token == 'desde' : 
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
	elif token == 'id' : 
		emparejar('id')
		emparejar('tk_dos_puntos')
		EXPRE()
		SENTENCIAS()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('SENTENCIAS')
def EXPRE(): 
 	if  token == 'tk_mayor' or token == 'tk_mayor_igual' or token == 'tk_menor' or token == 'tk_menor_igual' or token == 'tk_igual_que' or token == 'tk_suma' or token == 'tk_resta' or token == 'tk_potenciacion' or token == 'tk_modulo' or token == 'tk_division' token == 'tk_mayor' or token == 'tk_mayor_igual' or token == 'tk_menor' or token == 'tk_menor_igual' or token == 'tk_igual_que' or token == 'tk_suma' or token == 'tk_resta' or token == 'tk_potenciacion' or token == 'tk_modulo' or token == 'tk_division' token == 'tk_mayor' or token == 'tk_mayor_igual' or token == 'tk_menor' or token == 'tk_menor_igual' or token == 'tk_igual_que' or token == 'tk_suma' or token == 'tk_resta' or token == 'tk_potenciacion' or token == 'tk_modulo' or token == 'tk_division' or token == 'and' or token == 'or' : 
		EXPRE()
		OPER()
		EXPRE()
		AND()
	elif token == 'tk_parentesis_izquierdo' : 
		emparejar('tk_parentesis_izquierdo')
		EXPRE()
		emparejar('tk_parentesis_derecho')
	elif token == 'tk_numero' : 
		emparejar('tk_numero')
	elif token == 'tk_cadena' : 
		emparejar('tk_cadena')
	elif token == 'id' : 
		emparejar('id')
	else: errorSintaxis('EXPRE')
def AND(): 
 	if  token == 'and' : 
		emparejar('and')
		EXPRE()
	elif token == 'or' : 
		emparejar('or')
		EXPRE()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('AND')
def OPER(): 
 	if  token == 'tk_mayor' : 
		emparejar('tk_mayor')
	elif token == 'tk_mayor_igual' : 
		emparejar('tk_mayor_igual')
	elif token == 'tk_menor' : 
		emparejar('tk_menor')
	elif token == 'tk_menor_igual' : 
		emparejar('tk_menor_igual')
	elif token == 'tk_igual_que' : 
		emparejar('tk_igual_que')
	elif token == 'tk_suma' : 
		emparejar('tk_suma')
	elif token == 'tk_resta' : 
		emparejar('tk_resta')
	elif token == 'tk_potenciacion' : 
		emparejar('tk_potenciacion')
	elif token == 'tk_modulo' : 
		emparejar('tk_modulo')
	elif token == 'tk_division' : 
		emparejar('tk_division')
	else: errorSintaxis('OPER')
def ELSE(): 
 	if  token == 'sino' : 
		emparejar('sino')
		SENTENCIAS()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('ELSE')
def CASO(): 
 	if  token == 'caso' : 
		emparejar('caso')
		emparejar('tk_parentesis_izquierdo')
		EXPRE()
		emparejar('tk_parentesis_derecho')
		SENTENCIAS()
		CASO()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('CASO')
def INCREMENTO(): 
 	if  token == 'paso' : 
		emparejar('paso')
		EXPRE()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('INCREMENTO')
def ARGUMENTOS(): 
 	if  token == 'tk_numero' : 
		emparejar('tk_numero')
		ARGUMENTOS2()
	elif token == 'tk_cadena' : 
		emparejar('tk_cadena')
		ARGUMENTOS2()
	elif token == 'id' : 
		emparejar('id')
		ARGUMENTOS2()
	else: errorSintaxis('ARGUMENTOS')
def ARGUMENTOS2(): 
 	if  token == 'tk_coma' : 
		emparejar('tk_coma')
		ARGUMENTOS()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('ARGUMENTOS2')
def SUBRUTINAS(): 
 	if  token == 'subrutina' : 
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
 	if  token == 'ref' : 
		emparejar('ref')
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('REF')
def EXPRESUB(): 
 	if  token == 'tk_dos_puntos' : 
		ID()
		emparejar('tk_dos_puntos')
		TIPODATO()
		EXPRESUB2()
	else: errorSintaxis('EXPRESUB')
def EXPRESUB2(): 
 	if  token == 'tk_punto_y_coma' : 
		emparejar('tk_punto_y_coma')
		EXPRESUB()
	elif token == 'epsilon' : 
		pass 
	else: errorSintaxis('EXPRESUB2')
def VALOREF(): 
 	if  token == 'retorna' : 
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
	elif token == 'inicio' : 
		ESPECIFICACION()
		emparejar('inicio')
		SENTENCIAS()
		emparejar('fin')
	else: errorSintaxis('VALOREF')
entrada = input() 
tokenLexico = Lexico.lexico(entrada)
A = tokenLexico
token = getNextToken()