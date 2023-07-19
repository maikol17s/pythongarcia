def diccionarioExcepciones():
    dic = {}
    try:
        while True:
            clave = input('Ingrese una clave: ')
            if clave in dic:
                print('No se puede agregar una clave duplicada')
                print()
            else:
                valor = input('Ingrese el valor de la clave:')
                dic[clave] = valor 
    except:
        print('Ha ocurrido un error.')
    print(f'DICCIONARIO: {dic}')

    print()

    while True:
        try:
            clave_buscada = input('Ingrese la clave que desea buscar en el diccionario: ')
            valor_encontrado = diccionario[clave_buscada]
            print(f'La clave {clave_buscada} tiene el valor {valor_encontrado}.')
        except KeyError:
            print('La clave que desea encontrar no existe.')
        except:
            print('Ha ocurrido un error.')
        print('--- FIN ---')

diccionarioExcepciones()