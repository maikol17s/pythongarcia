#Ejercicio 11
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))

cociente=0
residuo=0

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor= num1
    menor=num2 

while mayor >= menor:
    mayor -= menor
    cociente +=1

residuo = mayor 

print(f'El cociente es: {cociente}')
print(f'El residuo es: {residuo}')