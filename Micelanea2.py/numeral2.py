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
        return " La suma es igual "

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

def mayorlista(l1,l2):
    num1 = maylista(l1)
    num2 = maylista(l2)
    for i in l1 and l2:
        if num1 > num2:
            return num1
        elif  num2 > num1:
            return num2
        else:
            return f'El numero es igual'

def menorlista(l1, l2):
    num1 = menlista(l1)
    num2 = menlista(l2)
    for i in l1 and l2:
        if num1 < num2:
            return num1
        elif  num2 < num1:
            return num2
        else:
            return f'El numero es igual'

def prolista(l1):
    return sumalista(l1)/len(l1)

def prolista(l2):
    return sumalista(l2)/len(l2)

def promtotal1(l1, l2):
    sumatotal= sumalista(l1) + sumalista(l2)
    sumatam= len(l1) + len(l2)
    totalprom= sumatotal / sumatam
    print(f'el promedio conjunto es : {totalprom}')

    if prolista(l1) < totalprom:
        return 'El promedio de la primera lista esta por debajo del promedio total'
    elif prolista(l1) == totalprom or prolista(l2) == totalprom:
        return 'El promedio de la lista y el promedio total son iguales'
    else:
        prolista(l1) > totalprom
        return 'El promedio de la primera lista esta por encima del promedio total'
   
def promtotal2(l1, l2):
    sumatotal= sumalista(l1) + sumalista(l2)
    sumatam= len(l1) + len(l2)
    totalprom= sumatotal / sumatam

    if prolista(l2) < totalprom:
        return 'El promedio de la segunda lista esta por debajo del promedio total'
    elif prolista(l1) == totalprom or prolista(l2) == totalprom:
        return 'El promedio de la lista y el promedio total son iguales'
    else:
        return 'El promedio de la segunda lista esta por encima del promedio total'

def numpar(lista):
    par=0
    for i in lista:
        if i % 2 == 0:
            par+=1
    return par

def numimpar(lista):
    impar=0
    for i in lista:
        if i % 2 == 1:
            impar+=1
    return impar
    
def mayorpar():
    mayor_pares = 0
    if numpar(l1) > numpar(l2):
        mayor_pares = numpar(l1)
    else:
        mayor_pares = numpar(l2)
    return  mayor_pares

def mayorimpar():
    mayor_impares = 0
    if numimpar(l1) > numimpar(l2):
        mayor_impares = numimpar(l1)
    else:
        mayor_impares = numimpar(l2)
    return  mayor_impares

l1=llenarlista(10,50)
l2=llenarlista2(10,50)
print(l1)
print(l2)
print()
print('La suma de la primera lista es: ',sumalista(l1))
print('La suma de la segunda lista es: ',sumalista(l2))
print('La suma mayor es: ',sumamayor(l1,l2))
print()
print('El mayor de la primera lista es: ',maylista(l1))
print('El mayor de la segunda lista es: ',maylista(l2))
print('El menor de la primera lista es: ',menlista(l1))
print('El menor de la segunda lista es: ',menlista(l2))
print()
print('El numero mayor de las listas es: ',mayorlista(l1,l2))
print('El numero menor de las listas es: ',menorlista(l1,l2))
print()
print('El promedio de la primera lista es: ',prolista(l1))
print('El promedio de la primera lista es: ',prolista(l2))
print()
print(promtotal1(l1, l2))
print(promtotal2(l1, l2))
print()
print(f'La primera lista tiene {numpar(l1)} pares')
print(f'La segunda lista tiene {numpar(l2)} pares')
print(f'La primera lista tiene {numimpar(l1)} impares')
print(f'La segunda lista tiene {numimpar(l2)} impares')
print(f'La lista que tiene mas pares es: {mayorpar()}')
print(f'La lista que tiene mas impares es: {mayorimpar()}')