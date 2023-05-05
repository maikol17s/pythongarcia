import random
lista=[]
cuadrado=[]
tam=random.randint(5,10)           # se generara una lista aleatoria en el de 5 a 10 elementos de longitud 
print(tam)
for i in range(tam):
    num=random.randrange(100)
    lista.append(num)
print(lista)

for i in range(len(lista)):       #los elemntos de la lista seran aleatorios son hasta 100
    cuadrado.append(lista[i]**2)
    #lista[i]=lista[i]**2
    # print(lista[i]*lista[i])
    # print(lista[i]**2)
    # print(math.pow(lista[i],2))

print(cuadrado)
print(sum(lista))