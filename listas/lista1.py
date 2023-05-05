import random
import math
import statistics

lista=[]
#Suma y promedio de la lista
suma=0
prom=0
#El mayor y el menor de la lista
mayor=0
menor=100
#moda y media de la lista
repeticion=0
media=0
#Division estandar
resta=0
division=0
cuadrado=2


tam=random.randint(5,5)
print(tam)
for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
print(lista)

for i in range(len(lista)):
    suma+=lista[i]
    prom=suma/len(lista )
print(f'La suma es: {suma}')
print(f'El promedio es: {prom}')

for i in lista:
    if i>mayor:
        mayor=i
    if i<menor:
        menor=i
print(f'El mayor es: {mayor}')
print(f'El menor es: {menor}')

for n in lista:
    modas=0
    for i in lista:
        if n == i:
            modas +=1
    if modas > repeticion:
        repeticion = modas
        moda = n
print ("La moda es: ", moda )

for i in range(len(lista)):
    media=suma/len(lista)
print(f'La media es: {media}')

for i in lista:
    i = resta - (suma) / (prom)
    cuadrado = resta ** 2
    suma += cuadrado
    division = suma / prom
raiz = math.sqrt(division)
print((f'La desviacion estandar es: {raiz}'))
