import re
import sys

def imprimir_token (): # función para imprimir de acuerdo al tipo de token
    global tipo_token, cadena,fila,columna
    if tipo_token == 'id':
        print("<id,{},{},{}>".format(cadena,fila, columna))
        cadena= ''
        tipo_token='nulo'
    elif tipo_token == 'tk_cadena':
        print("<tk_cadena,{},{},{}>".format(cadena,fila, columna))
        cadena= ''
        tipo_token='nulo'
    elif tipo_token == 'tk_numero':
        print("<{},{},{},{}>".format(tipo_token,cadena,fila, columna))
        cadena= ''
        tipo_token='nulo'
    elif tipo_token == 'posible' or tipo_token == 'nulo':
        print(">>> Error lexico(linea:{},posicion:{})".format(fila,columna))
        sys.exit()
    else:
        print("<{},{},{}>".format(tipo_token, fila, columna))
        cadena= ''
        tipo_token='nulo'
    return

# Este es un conjunto de palabra reservadas
palabras_reservadas = [
    'and', 'archivo', 'caso', 'const', 'constantes', 'desde', 'eval', 'fin',
    'hasta', 'inicio', 'lib', 'libext', 'matriz', 'mientras', 'not', 'or',
    'paso', 'subrutina', 'programa', 'ref', 'registro', 'repetir', 'retorna', 'si',
    'sino', 'tipos', 'var', 'variables', 'vector', 'numerico', 'imprimir', 'tan', 'logico',
    'TRUE', 'FALSE', 'SI', 'NO', 'leer', 'cadena', 'dim', 'int', 'cos', 'sin', 'cls', 'set_ifs', 
    'abs', 'arctan', 'ascii','dec', 'eof', 'exp', 'get_ifs', 'inc', 'log', 'lower', 'mem',
    'ord', 'paramval', 'pcount', 'pos', 'random', 'sec', 'set_stdin', 'set_stdout', 'sqrt',
    'str', 'strdup', 'strlen', 'substr', 'upper', 'val', 'alen'
]

#Un diccionario para acceder al nombre de cada token especial
tokens_especiales = {
    '=' : 'tk_asignacion',          ',': 'tk_coma',                  ']' : 'tk_corchete_derecho',
    '[' : 'tk_corchete_izquierdo',  '<>' : 'tk_distinto_de',         '/' : 'tk_division',
    ':' : 'tk_dos_puntos',          '==': 'tk_igual_que',            '}' : 'tk_llave_derecha',
    '{' : 'tk_llave_izquierda',     '>' : 'tk_mayor',                '>=' : 'tk_mayor_igual',
    '<' : 'tk_menor',               '<=' : 'tk_menor_igual',         '%' : 'tk_modulo',           '*': 'tk_multiplicacion',
    ')' : 'tk_parentesis_derecho',  '(' : 'tk_parentesis_izquierdo', '^' : 'tk_potenciacion',
    '.' : 'tk_punto',               ';' : 'tk_punto_y_coma',         '-' : 'tk_resta',            '+' : 'tk_suma'
    }



tipo_token = 'nulo'
cadena=''
lineas= []
fila = 0 
columna = 0
contador_col =  0
contador_fil = 0
multilinea = 0
token_cadena= 0
distinto = 0
numero_caracteres= 0

identificadores = re.compile(r'[A-Za-zñÑ_]+[A-Za-zñÑ0-9_]*')  # Expresión regular para el lenguaje que acepta los identificadores del lenguaje
numero = re.compile(r'(\d+(\.?\d*))?([eE][\+,\-]?(\d*?))?')   # Expresión regular que acepta el lenguaje de los numeros aceptados por el lenguaje SL
cadenas = re.compile(r'("[\s\S]*")|(\'[\s\S]*\')')            # Expresión regular que acepta las cadenas encerradas por comillas ""''
posible_numero = re.compile(r'(\d+(\.?\d*))?([eE][+-]?)')     # Expresión regular que ayuda a ir procesando los numeros que pueden estar escritos en
                                                              # notación cientifica 

# Bucle para leer las entradas.
while True:
    try:
        entrada = input()
    except EOFError:
        break
    entrada.rstrip('\n')     # Se aprovecha para quitar los \n al fianl de cada linea
    lineas.append([entrada]) # se hace una lista de lineas para contar las filas


# Aqui empieza el bucle para procesar las lineas
for i in lineas:
    contador_col=0  # estos contadores se utilizan para contar las columnas y filas
    contador_fil+=1

    # Cuando pasa por esta sección es el inicio de una linea, se verifica que la ultima cadena
    # antes de la linea se haya procesado , si no esta vacia, se verifica el tipo de token y se imprime
    if cadena != '' and not token_cadena :
        if cadena in palabras_reservadas:
            tipo_token = cadena
        elif cadena in tokens_especiales.keys():
            tipo_token = tokens_especiales[cadena]
        imprimir_token()
    elif token_cadena:
        print(">>> Error lexico(linea:{},posicion:{})".format(fila,columna))
        sys.exit()
    
    # Se procesa la palabra k en la linea i
    for k in i: 

        # Se empieza a procesar cada letra j en la palabra k
        for j in k: 
            contador_col+=1  # Cada letra que se lee es una columna mas

            # si la variable multilinea esta en 1 , se ha empezado a leer un comentario multilinea.
            if multilinea:
                if j=='*':
                    cadena+=j
                    continue
                elif j=='/':
                    cadena+=j
                    if cadena == '*/':
                        multilinea=0
                        cadena=''
                        continue
                    cadena=''
                continue
            # Si la cadena está vacia se guarda el valor del contador de columan ya que es el inicio de una palabra.
            elif cadena=='':
                columna=contador_col
                fila = contador_fil
                numero_caracteres=0

            # se agrega la letra j en la cadena.
            cadena+=j
            numero_caracteres+=1

            # Si encontramos unas comillas activamos la variable token_cadena en 1
            if j=='"' or j=="“" or j=="'" or token_cadena :
                if not token_cadena:
                    token_cadena=1
                
                # y mientras el token_cadena esta activo , se verifica si cumple con las restricciones de cadenas
                elif cadenas.fullmatch(cadena): 
                    tipo_token='tk_cadena'
                    token_cadena=0
                    continue
                else:
                    continue

            # Si encontramos un slash , verificamos si puede ser el inicio de un comentario    
            elif j=='/':
                if cadena=='//':
                    cadena=''
                    break
                continue
            elif j=='*':
                if cadena=='/*':
                    cadena=''
                    multilinea=1
                    continue

            # Si es un simbolo que pueda ser un token doble, se agrega a la cadena y se verifica en el siguiente ciclo 
            elif j=='<' and len(cadena)==1:
                continue
            elif j=='=' and len(cadena)==1:
                continue
            elif j=='>' and len(cadena)==1:
                continue

            # Se verifica si la cadena hasta el momento cumple con determinado tipo de token:
            elif identificadores.fullmatch(cadena) and numero_caracteres<33 :
                tipo_token = 'id'
                continue
            elif posible_numero.fullmatch(cadena):
                tipo_token= 'posible'
                continue
            elif numero.fullmatch(cadena):
                tipo_token= 'tk_numero'
                continue
            
            # si la cadena hasta el momento no cumple con ningun tipo de token, se verifica si es un token doble
            if cadena!='<>' and cadena!='<=' and  cadena!='>=' and cadena!='==':
                cadena=cadena[:-1]
            else:
                distinto=1
            if cadena in palabras_reservadas:
                tipo_token = cadena
            elif cadena in tokens_especiales.keys():
                tipo_token = tokens_especiales[cadena]
            
            # Si se llega a esta sección y la cadena no esta vacia se verifica si hasta el 
            # momento la cadena tiene un tipo de token activo.
            if cadena != '':
                imprimir_token()
            if j != ' ' and not distinto:
                
                # si el j es vacio, se verifica si la cadena hasta el momento cumple con algun tipo de token
                if cadena=='':
                    columna=contador_col
                    fila = contador_fil
                    numero_caracteres=0
                cadena+=j
                numero_caracteres+=1
                if cadena in tokens_especiales.keys():
                    tipo_token = tokens_especiales[cadena]
                elif identificadores.fullmatch(cadena) :
                    tipo_token = 'id'
                elif posible_numero.fullmatch(cadena):
                    tipo_token= 'posible'
                elif numero.fullmatch(cadena):
                    tipo_token= 'tk_numero'
            else: 
                distinto = 0 


# Al terminar el bucle for, se verifica si falta alguna cadena por procesar.
if cadena != '':
    if multilinea:
        sys.exit()
    if cadena in palabras_reservadas:
        tipo_token = cadena
    elif cadena in tokens_especiales.keys():
        tipo_token = tokens_especiales[cadena]
    elif identificadores.fullmatch(cadena) :
        tipo_token = 'id'
    elif posible_numero.fullmatch(cadena):
        tipo_token= 'posible'
    elif numero.fullmatch(cadena):
        tipo_token= 'tk_numero'
    imprimir_token()