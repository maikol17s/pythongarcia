#Ejercico 2
num=int(input("Ingresa un número: "))
i=2
x=0
while (x==0 ) and ( i < num):
        if num % i== 0:
            x=1
        else:
            i = i + 1
        print('El numero No es primo')

if x==0:
      print('El numero Es primo ')



