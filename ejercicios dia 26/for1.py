#Se declara las variables
comienzo  = int(input("Ingrese numero de partida: "))
fin = int(input("Ingrese numero final: "))
incremento= int(input("Ingrese el valor a incrementar: "))
decremento= int(input("Ingrese valor a decrementar: "))
n = int(input("ingrese un numero entero postivo: "))

#Inicio del ciclo for 
for i in range (comienzo, fin, incremento or decremento):
    if i%n==0:         #
        print(f'{i} Es multiplo de: {n}')
        i+=1
    else:
        print(i)
        