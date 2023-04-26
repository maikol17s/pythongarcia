num1,num2=100,50
print('1-sumar')                                
print('2-restar')
print('3-multiplicar')
print('4-dividir')
print('5-residuo')
op=int(input('que operacion?'))
match op:       # esta condicion sirve para simplificar una cadema de varios condicionales if, elif, else.
                # se pone match con el nombre de la varable
    case 1:                    
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:                          
        print(num1*num2) # se utiliza un case por cada operacion que puede pedir el usuario, asi evitando utilizar una cadena anidada de condicionales (if, elif, else)
    case 4:
        print(num1/num2)
    case 5:    
        print(num1%num2)

