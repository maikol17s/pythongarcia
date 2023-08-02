import csv

Mascotas = [
    ['Cometa', 'Perro', 'Adoptado'],
    ['Pelusa', 'Gato', 'En adopcion'],
    ['Bruno', 'Perro', 'Adoptado']
]

nombreArchivo = 'Mascotas.csv'

with open(nombreArchivo, "w") as file:
    writer = csv.writer(file)

    # Escribir el encabezado
    writer.writerow(['Nombre', 'Tipo', 'Estado'])

    # Escribir los datos de las comidas
    writer.writerows(Mascotas)

print(f'El archivo {nombreArchivo} se creo correctamente.')