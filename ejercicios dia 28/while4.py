#Ejercicio 3
num=int(input('Ingrese un numero: '))
i=2
suma=0
while i <= num:
    if num % i == 0:
        suma += num // i
    i+=1
if suma == num:
        print(f'Es perfecto: {num} ')
else:
    print(f'No es perfecto : {num} ')