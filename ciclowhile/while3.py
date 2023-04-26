i=1            #se declara variables
n=int(input('Ingrese numero: '))  #variable ingresada por el usuario la cual sera el nunmero de las veces que se repite

while i<n:     #el cicclo se repite hasta el numero que ingreso el usuario
    if i%7==0:  #es una condicion la cual mostrara cuales numeros son multiplos de 7
        print(f'{i} Es multiplo ')
    else:
        print(i)
        i+=1   #incrementa de uno en uno