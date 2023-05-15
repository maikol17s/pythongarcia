import random

def llenarlista(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def llenarlista2(tam,rango):
    lista=[]
    lista=[random.randrange(rango) for i in range(tam)]
    return lista

def sumalista(lista):
    sum=0
    for i in lista:
        sum+=i
    return sum

def sumamayor(l1, l2):
    sum1 = sum (l1)
    sum2 = sum (l2)
    if sum1 > sum2:
        return sum1
    elif sum1 < sum2:
        return sum2
    else:
        return " las dos listas tienen la misma suma. "

def maylista(lista):
    maximo=lista[0]
    for i in lista:
        if i>maximo:
            maximo=i
    return maximo

def maylista2(lista):
    maximo2=lista[0]
    for i in lista:
        if i>maximo2:
            maximo2=i
    return maximo2

def menlista(lista):
    minimo=lista[0]
    for i in lista:
        if i<minimo:
            minimo=i
    return minimo

def menlista2(lista):
    minimo2=lista[0]
    for i in lista:
        if i<minimo2:
            minimo2=i
    return minimo2

def maxmayor():
    mayor=0
    mayor2=0
    for i in l1 and l2:
        if l1 > 12:
            mayor = l1
            return mayor
        else:
            mayor2 = l2
            return mayor2
def maxmenor():
    menor=100
    menor2=100
    for i in l1 and l2:
        if menlista > menlista2:
            menor = menlista
            return menor        
        else:
            menor2 = menlista2
            return menor

def prolista(lista):
    return sumalista(l1)/len(l1)

def prolista2(lista):
    return sumalista(l2)/len(l2)

def promediototal(lista):
    return prolista(l1) + prolista2(l2)



l1=llenarlista(5,10)
l2=llenarlista2(5,10)
print(l1)
print(l2)
print()
print('La suma de la primera lista es: ',sumalista(l1))
print('La suma de la segunda lista es: ',sumalista(l2))
print('La suma mayor es: ',sumamayor(l1,l2))
print('El mayor de la primera lista es: ',maylista(l1))
print('El mayor de la segunda lista es: ',maylista(l2))
print('El menor de la primera lista es: ',menlista(l1))
print('El menor de la segunda lista es: ',menlista(l2))
print('El numero mayor de las listas es: ',maxmayor)
print('El numero menor de las listas es: ',maxmenor)
print('El promedio de la primera lista es: ',prolista(l1))
print('El promedio de la primera lista es: ',prolista2(l2))
print('El promedio total es: ',promediototal(l1,l2))
