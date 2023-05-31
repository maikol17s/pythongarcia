diccionario_español_ingles = {}
diccionario_ingles_español = {}

def agregar_animal(clave, valor ):

    diccionario_español_ingles[clave] = valor
    diccionario_ingles_español[valor] = clave

    return diccionario_español_ingles, diccionario_ingles_español   


def traducir_español_ingles():
    palabra = input("Ingrese una palabra en español: ")
    if palabra in diccionario_español_ingles:
        traduccion = diccionario_español_ingles[palabra]
        print(f"Traducción al inglés: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")

def traducir_ingles_español():
    palabra = input("Ingrese una palabra en inglés: ")
    if palabra in diccionario_ingles_español:
        traduccion = diccionario_ingles_español[palabra]
        print(f"Traducción al español: {traduccion}")
    else:
        print("La palabra no se encuentra en el diccionario.")