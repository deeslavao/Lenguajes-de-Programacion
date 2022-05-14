import os
import Lexico
from prediccion import get_prediccion
from gramatica import gramatica, palabras_reservadas, tokens_especiales

file = open("Analizador_sintactico/main.py", "w")

file.write("from Lexico import lexico\n")
file.write("from prediccion import get_prediccion\nprediccion,primeros,siguientes = get_prediccion()\n")


file.write ("def emparejar(letra): \n    if token.lexema == letra: \n")
file.write ("        token = getNextToken()\n    else:\n        errorSintaxis(letra)\n")

file.write ("def getNextToken():\n    if len(tokenLexico) == 0:\n        return '$'\n    else: return tokenLexico.pop(0)\n")

file.write("def errorSintaxis(regla): \n    return prediccion[regla]\n")
listgram=list(gramatica)

conjuntos,primeros,siguientes = get_prediccion()

for regla in list(conjuntos):
    file.write(f"def {regla}(): \n",)
    file.write(f"    if  ") 
    for primero in primeros[regla]:
        
        for valor in primero:
            if primero.index(valor) == 0:
                file.write(f"token.lexema == '{valor}' ")
            else:
                file.write(f"or token.lexema == '{valor}' ")
        file.write(": \n")
        

        for letra in gramatica[regla][primeros[regla].index(primero)]:
            if letra == 'epsilon':
                file.write(f"        pass \n")
            elif letra in palabras_reservadas or letra in tokens_especiales:
                file.write(f"        emparejar('{letra}')\n")
            else:
                file.write(f"        {letra}()\n")
        file.write(f"    elif ")
    
    file.seek(file.tell()-len("    elif "))
    file.truncate()
    file.write(f"    else: errorSintaxis('{regla}')\n")


file.write("tokenLexico = lexico()\n")
file.write("token = getNextToken()\n")
file.write("INICIO()\n")
file.write("if token.lexema != '$':\n    print('Error sintactico: falta inicio')\n    exit()\n\n")
file.write("print('El analisis sintactico ha finalizado exitosamente.')")
