import math
def FormuCuadratica():
    while True:
        try:
            a=float(input('Ingrese el numero: '))
            b=float(input('Ingrese el segundo numero: '))
            c=float(input('Ingrese el tercer numero: '))
            x1=math.sqrt (b ** b)-(4*a*c) 
            x2=-b - x1
            x3= 2*(a)
            resul= x2 / x3
            print(f'El resultado es {resul}')
        except ZeroDivisionError:
            print('Imposible dividir en cero')
        except ValueError:
            print('Valor no valido')
        
        print('Fin')

print(FormuCuadratica())