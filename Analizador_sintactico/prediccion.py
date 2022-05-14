from gramatica import gramatica, palabras_reservadas, tokens_especiales
#from gramatica_de_prueba import gramatica, palabras_reservadas, tokens_especiales

primeros= {}
primeros2= {}

siguientes={}

prediccion={}

def generar_primeros ():
    
    for g in palabras_reservadas:
        primeros[g]=[g]
        primeros2[g]=[[g]]
    for g in tokens_especiales:
        primeros[g]=[g]
        primeros2[g]=[[g]]

    primeros['epsilon'] = ['epsilon']
    primeros2['epsilon'] = [['epsilon']]
    for b in list(gramatica):
        primeros[b]=[]
        primeros2[b]=[]
    auxiliar=[]
    for i in reversed(list(gramatica)):
        for j in gramatica[i]:
            for h in j:
                if h == 'epsilon' and len(j) == 1:
                    primeros[i].append('epsilon')
                    primeros2[i].append(['epsilon'])
                    break
                elif h in palabras_reservadas or h in tokens_especiales:
                    primeros[i].append(h)
                    if len(auxiliar)==0:
                        primeros2[i].append([h])
                    else:
                        auxiliar.extend([h])
                    break
                elif h in gramatica.keys():
                    primeros[i].extend(primeros[h])
                    auxiliar.extend(primeros[h])
                    if 'epsilon' in primeros[h]:
                        primeros[i].remove('epsilon')
                        auxiliar.remove('epsilon')
            if len(auxiliar)!=0:            
                primeros2[i].append(auxiliar)
                auxiliar=[] 

def generar_siguientes():
    lisGrama= list(gramatica)
    for g in lisGrama:
        siguientes[g]=[]

    for i in lisGrama:
        if lisGrama.index(i)==0:
            siguientes[i].append('$')
        for j in lisGrama:
            values= gramatica[j]
            for h in values:
                for k in h:
                    if k == i :
                        if h.index(k) == len(h)-1:
                            siguientes[k].extend(siguientes[j])
                            break
                        elif 'epsilon' in primeros[h[h.index(k)+1]]:
                            siguientes[i].extend(primeros[h[h.index(k)+1]])
                            siguientes[i].remove('epsilon')
                            siguientes[i].extend(siguientes[j])
                        else:
                            siguientes[i].extend(primeros[h[h.index(k)+1]])


def generar_prediccion():
    noter=0
    auxiliar=[]
    lisGrama= list(gramatica)
    for b in list(gramatica):
        prediccion[b]=[]
    for i in lisGrama:
        
        for j in gramatica[i]:
            for h in j:
                if (h in palabras_reservadas or h in tokens_especiales) and noter == 1:
                    noter = 0
                    auxiliar = []
                    break
                elif (h in palabras_reservadas or h in tokens_especiales):
                    prediccion[i].append([h])
                    break
                elif "epsilon" in primeros[h] and len(j) == 1:
                    auxiliar.extend(siguientes[i])
                    prediccion[i].append(auxiliar)
                    break
                else:
                    noter=1
                    if 'epsilon' in primeros[h]:
                        auxiliar.extend(primeros[h])
                        auxiliar.remove('epsilon')                       
                    else:
                        auxiliar.extend(primeros[h])
            if noter:
                if 'epsilon' in auxiliar:
                    auxiliar.remove('epsilon')
                    auxiliar.extend(siguientes[i])
                    prediccion[i].append(auxiliar)
                    print("aqui")
                else:
                    prediccion[i].append(auxiliar)
                    noter = 0
                    auxiliar = [] 
                           


        
        
def get_prediccion():
    generar_primeros()
    generar_siguientes()
    generar_prediccion()
    for i in list(gramatica):
        siguientes[i] = list(set(siguientes[i]))
    return prediccion,primeros2,siguientes

generar_primeros()
generar_siguientes()
generar_prediccion()
'''
for i in list(gramatica):
   print (i, end=' - ')
   print (primeros[i])
print("\n primeros2 \n")
print("\n primeros3 \n")
for i in list(gramatica):
    print (i, end=' - ')
    print (prediccion[i])

for i in list(gramatica):
   print (i, end=' - ')
   print (siguientes[i])'''