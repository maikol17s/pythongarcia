import random


def llenarlista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumalista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promediolista(lista):
    return sumalista(lista)/len(lista)


def maylista(lista):
    maximo=lista[0]
    for i in lista:
        if i>maximo:
            maximo=i
    return maximo

def menlista(lista):
    minimo=lista[0]
    for i in lista:
        if i<minimo:
            minimo=i
    return minimo

def moda(lista):
    max=0
    for n in lista:
        cont=0
        for o in lista:
            if n == o:
                cont+=1
        if cont > max:
            max = cont
            moda1= n
    return f'La moda es: {moda1} ya que se repite {max}'

def posicion(lista):
    repmoda=[]
    for n in range(len(l1)):
        if moda == l1[n]:
            repmoda.append(n)
    return f'La {moda} esta en la posicon {repmoda}'


def mediana(lista):
    if len(lista) %2!=0:
        pos = (len(lista)+1)//2
        return lista[pos-1]
    else:
        pos = (len(lista) - 1) // 2
        pos1 = (lista [pos])
        pos2 = (lista[pos + 1])
        pos = pos1 + pos2
        pos = pos / 2
    return pos

def ascendente(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

def descendente(lista):
    aux=0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

l1=llenarlista(5,10)
print(l1)
print(moda(l1))
print(f'La mediana es: ',mediana(l1))
print (f'El {moda} esta en la posicion {posicion}')
print()
print('La suma es:',sumalista(l1))
print('El promedio es:',promediolista(l1))
print('El mayor es: ',maylista(l1))
print('El menor es: ', menlista(l1))
print(ascendente(l1))
print(descendente(l1))