x,y=2,2
cont=1
resul=0
resul1=0
while not(x>y or y>x):
    print(f'Intento {cont}')
    x=int(input('Ingrese numero: '))
    y=int(input('Ingrese numero: '))
    cont=cont+1
    if x>y:
         print(f'El mayor es: {x}')
    else:
         print(f'El menor es: {x}')
         if y>x:
              print(f'El mayor es: {y}')
         else:
              print(f'El menor es: {y}')
while resul >=0:
             if resul==0:
               resul=x-y
               print(f'El resultado es: {resul}')
               if resul >0:
                 print('Se puede seguir respantdo ')
                 z=int(input("Ingrese el numero: "))
                 resul1=resul-z
                 if resul1 >0:
                     z=int(input("Ingrese el numero: "))
                     resul1=resul1-z
                     print(f'El resultado es: {resul1}')
               else:
                  print('no se puede segur restando')
                 
                 



