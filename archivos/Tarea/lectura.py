#Consultar como se manipulan archivos CSV. dos ejemplos lectura y escritura

#Lectura 

import csv

def leerArchivo(nombreArchivo):
    amigo = []
    with open(nombreArchivo) as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            amigo.append(fila)
    return amigo

nombreArchivo = 'Mascotas.csv'
amigo = leerArchivo(nombreArchivo)
for mascotas in amigo:
    print(f'Nombre: {mascotas["Nombre"]}, Tipo: {mascotas["Tipo"]}, Estado: {mascotas["Estado"]}')