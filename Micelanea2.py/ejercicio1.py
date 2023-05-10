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

def asc(l1):
    for i in l1:
        for j in range(i+1,20):
            if l1[i] > l1[j]:
                aux = l1[i]
                l1[i] = l1[j]
                l1[j] = aux
    return l1

l1=llenarlista(5,20)
print(l1)
print()
print('La suma es:',sumalista(l1))
print('El promedio es:',promediolista(l1))
print('El mayor es: ',maylista(l1))
print('El menor es: ', menlista(l1))
print(asc(l1))