#[], {}, (), {()}
x=100
print(type(x))  #type es una función que no esta enlasada a ningun objeto
x='Soacha'
print(type(x))                           #exiten dos tipos de listas homegeneas y heterogeneas 
lista=['python',100,[1,2,3,[]],'a']      #esta lista es heterogenea
print(type(lista))                       #se imprime el tipo de dato que es lista
print(len(lista))                        #la funcion len calcula la longitud de una lista 
print(lista[0])                          #se puede acceder a cada uno de los elementos de la lista por separado
print(lista[1])
print(lista[3])
print(lista[-4])                         #se accede a un elemento de atras hacia adelante 

del lista[-2]                            #la funcion del permite eliminar elementos de la lista
print(lista)

"""
cuenta1=cuenta()
cuenta2=cuenta()                         
cuenta3=cuenta()                        
cuenta1.deposit()                       #exiten metodos, que son funciones en lasadas a un objeto
print(type(cuenta1))
cuenta2.deposit()
cuenta3.deposit()
"""