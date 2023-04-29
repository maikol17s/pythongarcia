#Ejercicio 12
a=int(input("Ingrese un valor "))
for i in range(a):
    for j in range(i+1):
        print('*', end='')
    print()