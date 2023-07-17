import random
def listaError():
    while True:
        list=[]
        tam=random.randrange(5,9)
        list.append(tam)
        for i in range(tam):
            try:
                x=int(input('Escriba un indice de la lista: '))
                print('Imposible encontrar ese indice ')
            except IndexError:
                print('Indece no encontrad')
            except ValueError:
               print('Valor no valido')
        
        print('Fin')
print(listaError())