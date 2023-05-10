import random

lista=[]
lista2=[]
sum1,sum2 = 0, 0
prod1=0
prod2=0
mayor1, mayor2= 0, 0
menor1, menor2= 10000, 10000
par=0
impar=0
par2=0
impar2=0
#////////////////////////////////////#

tam=random.randint(15,20)
print(tam)
for i in range(tam):
    num=random.randrange(0,9)
    lista.append(num)
print(lista)

for i in lista:
    sum1+=lista[i]
    prod1=sum1/tam
print(f'La suma de la lista es: {sum1}')
print(f'El promedio de la lista es: {prod1}')

pares=[]
impares=[]
for i in lista:
    if i % 2 == 0:
        par+=1
        pares.append(i)
print(f'Los numeros pares son: {pares}')

for i in lista:
    if i % 2 == 1:
        impar+=1
        impares.append(i)
print((f'Los  numeros impares son: {impares}'))

#/////////////////////////////#

tam2=random.randint(15,20)
print(tam2)
for i in range(tam2):
    num2=random.randrange(0,9)
    lista2.append(num2)
print(lista2)

for i in lista2:
    sum2+=lista2[i]
    prod2=sum2/tam2
print(f'La suma de la lista es: {sum2}')
print(f'El promedio de la lista2 es: {prod2}')

pares2=[]
impares2=[]
for j in lista2:
    if j % 2 == 0:
        par2+=1
        pares2.append(j)
print(f'Los numeros pares son: {pares2}')

for j in lista2:
    if j % 2 == 1:
        impar2+=1
        impares2.append(j)
print(f'Los numeros impares son: {impares2}')
#/////////////////////////////////#

sumtotal = sum1 + sum2
print(f'La suma total es: {sumtotal}')

if sum1>sum2:
    max=sum1
if sum2>sum1:
    max=sum2
print(f'La suma mayor es: {max}')

for i in lista:
    if i > mayor1:
        mayor1 = i
    if i < menor1:
        menor = i
for i in lista2:
    if i > mayor2:
        mayor2 = i
    if i < menor2:
        menor2 = i
if mayor1 > mayor2:
    maxmayor = mayor1
else:
    maxmayor = mayor2
if menor1 > menor2:
    minmenor = menor2
else:
    minmenor = menor2
print(f'El numero mayor de las listas es: {maxmayor}')
print(f'El numero menor de las listas es: {minmenor}')

tamtotal = tam + tam2
prod = sumtotal / tamtotal
print(f'El promedio conjunto es: {prod}')

if prod1 > num:
     print(f'Esta por arriba del arreglo')
else:
    print(f'Esta por debajo del arreglo')

if prod2 > num2:
    print(f'Esta por arriba del arreglo')
else:
    print(f'Esta por debajo del arreglo')

if par > par2:
    print(f'La primera lista tiene un total de {par} pares')
else:
    print(f'La lista2 tiene un total de {par2} pares ')

if impar > impar2:
    print(f'La primera lista tiene un total de {impar} impares')
else:
    print(f'La lista2 tiene un total de {impar2} impares ')