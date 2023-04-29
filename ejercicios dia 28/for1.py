#Ejercicio 15
a=int(input("Ingrese un valor no negativo: "))
for i in range(a, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()