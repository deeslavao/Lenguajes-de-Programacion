import re 
import os
import sys

def lexico():

    operator_tokens = {
        "}" : "tk_llave_derecha",
        "{" : "tk_llave_izquierda",
        "<>" : "tk_distinto_de",
        "<" : "tk_menor",
        ">" : "tk_mayor",
        "<=" : "tk_menor_igual",
        ">=" : "tk_mayor_igual",
        "==" : "tk_igual_que",
        "+" : "tk_suma",
        "-" : "tk_resta",
        "/" : "tk_division",
        "*" : "tk_multiplicacion",
        "%" : "tk_modulo",
        ";" : "tk_punto_y_coma",
        ":" : "tk_dos_puntos",
        "(" : "tk_parentesis_izquierdo",
        ")" : "tk_parentesis_derecho",
        "[" : "tk_corchete_izquierdo",
        "]" : "tk_corchete_derecho",
        "," : "tk_coma",
        "^" : "tk_potenciacion",
        "." : "tk_punto",
        "=" : "tk_asignacion"
    }

    def isalphabetic(char):
        return (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122) or (char == "_")


    def isfloat(element):
        try:
            float(element)
        except ValueError:
            return False
        else:
            return True

    def isnumber(element):
        try: 
            int(element)
        except ValueError:
            try: 
                float(element)
            except ValueError:
                #print("es string")
                return False
            else:
                #print("es real")
                return True
        else:
            #print("es entero")
            return True

    reserved_words = ("numerico", "dim", "abs", "cos", "dec", "lower", "mem", "ord", "paramval", "pcount", "pos", "random", "sec", "set_stdin", "eof", "log", "get_ifs", "exp", "arctan", "int", "ascii", "ref", "inc", "arreglo", "alen", "cls", "leer", "tan", "cadena", "logico", "var", "imprimir", "and", "constantes", "upper", "val", "set_ifs", "hasta", "sin", "matriz", "paso", "registro", "sino", "vector", "archivo", "desde", "inicio", "mientras", "subrutina", "TRUE", "strdup", "strlen", "substr", "FALSE", "SI", "NO", "set_stdout", "sqrt", "str", "repetir", "tipos", "caso", "eval", "lib", "not", "programa", "retorna", "const", "fin", "libext", "or", "si", "variables")

    row = 1
    column = 1
    string = ""

    state = 0

    class Token:

        def __init__(self, row, column, lexema=None, token_id=None):
            self.row = row
            self.column = column
            self.lexema = lexema
            self.token_id = token_id

        def add_lexema(self, lexema):

            if isnumber(lexema):
                self.lexema = lexema
                if "." or "e" in lexema:
                    self.token_id = "tk_numero"
                else:
                    self.token_id = "tk_numero"
            elif lexema in operator_tokens:
                self.lexema = lexema
                self.token_id = operator_tokens[self.lexema]
            elif lexema in reserved_words:
                self.lexema = lexema
                self.token_id = None
            elif (lexema[0] == "'" or lexema[0] == '"') and ((lexema[-1] == "'" or lexema[-1] == '"')):
                self.lexema = lexema[0:]
                self.token_id = "tk_cadena"           
            else:
                self.lexema = lexema
                self.token_id = "id"

        def __str__(self):
            if self.token_id == None:
                return [str(self.lexema),str(self.row),str(self.column)]
            elif self.token_id == "tk_cadena":
                return [str(self.token_id),str(self.lexema),str(self.row),str(self.column)]
            elif self.token_id == "tk_numero" or self.token_id == "id":
                return [str(self.token_id),str(self.lexema),str(self.row),str(self.column)]
            else:
                return [str(self.token_id),str(self.row),str(self.column)]

    def error(r, c):
        print(">>> Error lexico(linea:" + str(r) + ",posicion:" + str(c) + ")")
        exit()

    def lexico(entrada):
        return entrada

    '''
    0 : Ninguno
    1 : alphabetic
    2 : numeric
    3 : special
    4 : cadena
    ''' 
    TokenList = []

    while True:
        try:
            actual = input()
            actual2 = actual
            pattern = "//"
            if re.search(pattern, actual): 
                h = re.search(pattern, actual)
                s = h.start()           
                actual = actual[:s]

            pattern2 = "/*"
            if actual[:2]==pattern2:
                a = 1
                ñ = 0
                while a == 1:  
                    b = actual[-2:]
                    c = "*/"                
                    d = c[-2:] 
                    #column += 1
                    for cha in actual:
                        
                        ñ = ñ+1

                        string += cha
                        column = ñ + 1
                        z = string[-2:]
                        if z == "*/":
                            actual = actual[ñ:]
                            a = 0
                            #column -= 2
                            string = ""
                            break                 
                    string = ""
                    if a == 0:
                        break
                    actual = input()
                    ñ=0
                    
                    row += 1
                #actual = ""            
                

        except EOFError:
            break
        else:        
            for char in actual:

                if state == 0:
                    if isalphabetic(char):
                        token = Token(row, column)
                        string += char
                        state = 1
                    elif char.isnumeric():
                        token = Token(row, column)
                        string += char
                        state = 2
                    elif char in operator_tokens:
                        token = Token(row, column)
                        string += char
                        state = 3
                    elif char == '"':
                        token = Token(row, column)
                        string += char
                        state = 4
                    elif char == "'":
                        token = Token(row, column)
                        string += char
                        state = 5
                    elif char == " " or char == "\r" or char == "\n" or char == "\'" or char == '\"':
                        pass
                    else:
                        error(row, column)


                elif state == 1:
                    if isalphabetic(char) or char == "_":
                        string += char
                    elif char.isnumeric():
                        string += char
                    elif char in operator_tokens:
                        
                        
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 3
                    elif char == '"':
                        
                        
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 4
                    elif char == "'" :
                        
                        
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 5
                    elif char == " " or char == "\r" or char == "\n" or char == "\'" or char == '\"':
                        
                        
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        string = ""
                        state = 0
                    else:
                        
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        error(row, column)


                elif state == 2:
                    
                    if char == "e" or char == "E" or char == "+" or char == "-"  :
                        string += char
                    
                    elif isalphabetic(char) or char == "_" and (char != "e" and char != "E"):
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 1

                    elif char.isnumeric() or char == ".":
                        string += char
                        if string.count(".") > 1:
                            error(token.row, token.column)
                    elif char in operator_tokens:

                        if string[-1] == ".":
                            error(row, column-1)
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 3
                    elif char == '"':
                        if string[-1] == ".":
                            error(row, column)
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 4

                    elif char == "'":
                        if string[-1] == ".":
                            error(row, column)
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 5

                    elif char == " " or char == "\r" or char == "\n" or char == "\'" or char == '\"':
                        if string[-1] == ".":
                            token.add_lexema(string[0:-1])
                            #print(token)
                            TokenList.append(token)
                            error(row, column-1)
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        string = ""
                        state = 0
                    else:
                        if string[-1] == ".":
                            error(row, column-1)
                        
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        error(row, column)

                elif state == 3:
                    if isalphabetic(char):
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 1
                    elif char.isnumeric():
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 2
                    elif char in operator_tokens:

                        if (string in operator_tokens) and (string != "<") and (string != ">") and (string != "/") and (string != "=") :
                            token.add_lexema(string)
                            #print(token)
                            TokenList.append(token)
                            token = Token(row, column)
                            string = ""

                        string += char
                        '''
                        if string not in operator_tokens and string != "/*" :
                            token = Token(row, column-1)
                            token.add_lexema(string[0])
                            print(token)
                            token = Token(row, column)
                            string = string[-1]
                        '''

                    elif char == '"':
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 4
                    elif char == "'":
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        token = Token(row, column)
                        string = ""
                        string += char
                        state = 5
                    elif char == " " or char == "\r" or char == "\n" or char == "\'" or char == '\"':
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        string = ""
                        state = 0
                    else:
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        error(row, column)

                elif state == 4:

                    string += char

                    if char == "\\":
                        state = 7

                    if char == '"':
                        token.add_lexema(string)                    
                        #print(token)
                        TokenList.append(token)
                        string = ""
                        state = 0

                elif state == 5:

                    string += char
                    if char == "\\":
                        state = 6

                    if char == "'":
                        token.add_lexema(string)
                        #print(token)
                        TokenList.append(token)
                        string = ""
                        state = 0

                elif state == 6:
                    if char == "'":
                        string += char
                        state = 5
                    else:
                        string += char
                        state = 5

                elif state == 7:
                    if char == '"':
                        string += char
                        state = 4
                    else:
                        string += char
                        state = 4



                column += 1
                
            if state == 4:  
                error(token.row, token.column)
            if state == 5:  
                error(token.row, token.column)

            if len(string) != 0 and state != 4:
                token.add_lexema(string)
                #print(token)
                TokenList.append(token)
                string = ""
                state = 0

            row += 1
            column = 1
            
        if state == 4:
            error(token.row, token.column)

    return TokenList