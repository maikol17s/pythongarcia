while True:
    try:
        x=float(input('Ingrese un numero: '))
        y=float(input('Ingrese un numero: '))
        if x/y or y/x:
            resu= x/y
            print(f'El resultado de la division es {resu}')
    except ZeroDivisionError:
        print('Imposible dividir en cero')
    except ValueError:
        print('Valor no valido')
    except:
        print('No se que hacer')
    print('Fin')