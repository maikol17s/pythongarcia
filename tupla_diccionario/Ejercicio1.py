dic={'carro':'Nissan GT-R.',
     'avion':'Pilatus PC-24',
     'moto':'KAWASAKI NINJA',
     'pais':'Dubai'}

def palabra(key, diction):
    if key  in diction:
        return f"La clave {key} no esta en el diccionario"
    else:
        f1 = diction[key]
        f2 = type(f1)
        if f2 is str:
            f2 = "Cadena"
        else:
            f2= "Entero"

        return f"La palabra {key} esta asociada a --> {f1} y es de tipo {f2}"
    
print(palabra(input("Escriba la clave a buscar: "), dic))