#Ejercicio 2

d1={}
d2={}

def agregar1(f1, clave, valor, diccionario):
    ani=0
    diccionario.update({clave:valor})
    while True:
        ani+=1
        clave = input('Escriba la clave: ')
        valor= input('Escriba un valor: ')
        diccionario.update({clave:valor})
        if ani == f1:
            break          
    return True

def agregar2(f2, clave, valor, diccionario):
    diccionario.update({clave:valor})

    for i in range(1, f2):
        clave = input('Escriba la clave: ')
        valor= input('Escriba un valor: ')
        diccionario.update({clave:valor})
    return True

def actualizar(diccionario):
    print()
    print('Diccionario:')
    for m1 in diccionario:
        claves = diccionario[m1]
        print(f"{m1} --> {claves}") 

print('Elija el diccionarios que desea llenar: ')
print('1')
print('2')

pregunta= int(input('Escriba la opcion que desea: '))

match pregunta:
    case 1:
        print('Escriba la palabra en español, y el significado en ingles')
        agregar1(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input('Escriba el valor: '),d1)
        actualizar(d1)
    case 2:
        print('Escriba la palabra en ingles, y el significado en español')
        agregar2(int(input('Cuantas veces quiere llenar el diccionario: ')), input('Escriba la clave: '), input("Escriba el valor: "),d2)
        actualizar(d2)  