import random

sum1=0
sum2=0

tam = random.randrange(20, 30)
lista = [round(random.random()*5,2)for i in range(tam)]
print(lista)
print()

nota=['aprobado' if i > 3 else 'desaprobado' for i in lista]

l1=lista[:5]
l2=nota[:5]
print(l1)
print(l2)

print()

l3=lista[5:]
l4=nota[5:]
print(l3)
print(l4)

print()

print('Aprobados')
aprobado=[i for i in lista if i>3] 
print(aprobado)
l5=lista[:5]
l6=aprobado[:5]
print()

print('Desaprobados')
desaprobado=[i for i in lista if i<3]
print(desaprobado)
l7=lista[5:]
l8=aprobado[5:]
print()

lista.sort()
print(lista)
print()

print('0 a 1')
uni1=[x for x in lista if x < 2]
print(uni1)

print()

print('1 a 2')
uni2=[x for x in lista if x > 1 and x < 3]
print(uni2)

print()

print('2 a 3')
uni3=[x for x in lista if x > 2 and x <4]
print(uni3)

print()

print('3 a 4')
uni4=[x for x in lista if x >3 and x <=5]
print(uni4)

print()

print('Suma Aprobados')
apro=[sum(aprobado)]
print(apro)

print()

print('Suma Desaprobados')
desa=[sum(desaprobado)]
print(desa)

print()

promApro=[sum(apro) / len(aprobado)]
promDesa=[sum(desa) / len(desaprobado)]
print(f'El promedio de aprobados es: {promApro}')
print(f'El promedio de desaprobados es: {promDesa}')