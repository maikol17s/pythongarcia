num=1
cont=0
sum=0
prom=0                                 #Se definen variables
menor=1000000
mayor=0
while num!=0:            #El numero que se ingresa es cualquiera
                         #El siclo termina cuando se ingresa 0
    num=int(input('ingrese numero: ')) 
    cont=cont+1
    sum=sum+num           
    if num>mayor:         #Se coloa una condicion para identificar el numero mayor ingresados
        mayor=num
    if num < menor:       #Se coloa una condicion para identificar el numero menor ingresado
        mayor=num
        menor=num
        
print(f'fueron ingresados: {cont-1} numeros')
print(f'La suma total es: {sum}')
print(f'El promedio es: {sum/(cont-1)}')
print(f'El numero mayor es: {mayor}')
print(f'El numero menor es: {menor}')