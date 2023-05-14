import random

def llenarlista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

l1=llenarlista(5,10)

def posicion(numero):
    listaIndices=[]
    cont=0
    veces=0
    for x in l1:
        if numero in l1:
            True
        else:
            return f"El {numero} no esta en la lista"
        cont+=1
        if numero == x:
            veces+=1
            posicion = cont-1
            listaIndices.append(posicion)
    return f"El {numero} si esta, esta {veces} veces, esta en la posicion {listaIndices}"
        
print(posicion(int(input("Escriba el numero: "))))
