import random 
import math 

raiz = []
potencia = []

tam = random.randint(5, 10)

lista =[random.randrange (100) for i in range (tam)]
lista2 = [i for i in lista]

par=  lista[2::2]
print (lista)

raiz  = [num ** 0.5 for num in lista]

print (raiz)

impares = lista2[::2]

pot = [num ** 2 for num in impares]
print(pot)