#Ejercicio 6
max= 0
while True:
    numero = int(input("Introduce el numero positivo: "))
    if numero < 0:
        break
    if numero > max:
        max = numero

print("El numero mayor ingresado es:", max)