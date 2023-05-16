import random

def llenarLista(tam,rango):
    lista=[]
    lista=[random.randint(100, 500) for i in range(tam)]
    return lista

l1 = llenarLista(30,50)


def ascendente(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

print(ascendente(l1))

def cuartil(lista):
    listaCuartil=[]
    cuart=0
    cuart2=0
    posicion=0
    rep=0
    rep2=0
    n=len(lista)
    for i in range(1,4):
        posicion=rep2
        cuart= (i * (n+1))/4
        print(cuart)
        cuart2=int(cuart)
        r=cuart2+1
        rep=(cuart+r)/2
        rep2=int(rep)
        print(rep2)
        if i == 1:
            listaCuartil=lista[ :rep2]
            print(f"Cuartil {i} {listaCuartil}")
        else:
            listaCuartil=lista[posicion:rep2]
            print(f"Cuartil {i} {listaCuartil}")

def quintil(lista):
    listaquintil=[]
    quint=0
    quint2=0
    posicion=0
    rep=0
    rep2=0
    n=len(lista)
    for i in range(1,4):
        posicion=rep2
        quint= (i * (n+1))/5
        print(quint)
        cuart2=int(quint)
        r=quint2+1
        rep=(quint2+r)/2
        rep2=int(rep)
        print(rep2)
        if i == 1:
            listaquinil=lista[ :rep2]
            print(f"Quintil {i} {listaquintil}")
        else:
            listaCuartil=lista[posicion:rep2]
            print(f"Quintil {i} {listaquintil}")

print(ascendente(l1))
cuartil(l1)
quintil(l1)