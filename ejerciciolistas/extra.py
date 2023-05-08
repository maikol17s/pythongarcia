import random

lista=[]
tam=random.randint(5,5)
for i in range(tam):
    num=random.randrange(10)
    lista.append(num)
#///////////////////////////#
num=int(input('Ingrese un numero: '))
while num not in lista:
    print('No esta en la lista')
    num=int(input('Ingrese un numero: '))

for i in range(tam):
    if num == lista[i]:
        break
print(f'El {num} si esta en la lista')
print(lista)
print(tam)

for c in lista:
    cont=0
    for a in lista:
        if num == a:
            cont+=1
if cont == 1:
    print((f'{num} no se repite'))
else:
    print(f'{num} se repite {cont}')

rep=[]
for i in range(len(lista)):
    if num == lista[i]:
        rep.append(i)
print(f'El numero {num} esta en la posicion {rep}')