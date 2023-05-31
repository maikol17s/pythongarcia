#a. Funcion para llenar una lista con numeros aleatorios

import random

def llenarLista(tam,rango):
    lista=[random.randrange(rango) for i in range(tam)]    
    return lista

#b. Funcion para sumar los elementos de una lista

def sumaLista(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

#c.Funcion para sacar el promedio de una lista 

def promedioLista(lista):
    return sumaLista(lista)/len(lista)

#d. Funcion para mostrar el mayor de una lista 

def mayor(lista):
    max=0
    for i in lista:
        if i>max:
            max=i
    return max

#e. Funcion para mostrar el menor de una lista

def menor(lista):
    min=100000
    for i in lista:
        if i<min:
            min=i
    return min
