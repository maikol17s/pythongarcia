import math

def FormulaCuadratica():
    while True:
        a=int(input('Ingrese el numero: '))
        b=int(input('Ingrese el segundo numero: '))
        c=int(input('Ingrese el tercer numero: '))
        x1=math.sqrt (b ** 2) - (4*a*b)
        x2=-b -x1
        x3=2*(a)
        resul= x2 / x3
        print(resul)

print(FormulaCuadratica())