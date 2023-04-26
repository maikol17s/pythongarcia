num,num2=7,9       #se decalran variables
cont=1             #esta pueden opcional 
while not(num % num2 == 0 or num2 % num==0):  #SE verifica si los numeros ingresados son factores     
    print(f'Intento {cont} ') 
    num= int(input('Ingrese un numero: '))    #Son variables ingresadas por el usuario
    num2= int(input('Ingres un numero: '))    #Son variables ingresadas por el usuario

    cont=cont+1                               #es una variable que ayuda a llevar los numeros de intentos que se  llevan 
print(f'{num} y {num2} son factor ')          #muestra los numeros ingresados con una frase que dice que son factor 
    
        

