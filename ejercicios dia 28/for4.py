#Ejercicio 1
x=int(input('Ingrese un numero: '))

for i in range(1,x):
    if x%i==0:
        print(i, "es divisor de: ", x)
    else:
        print(i)
        