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


def mayorlista(lista):
    mayor=0
    for i in lista:
        if i>mayor:
            mayor=i
    return mayorlista


def menorlista(lista):
    menor=100
    for i in lista:
        if i<menor:
            menor=i
    return menorlista

l1=llenarlista(5,20)
print(l1)
print()
print(sumalista(l1))
print(promediolista(l1))
print(mayorlista(l1))
print(menorlista(l1))