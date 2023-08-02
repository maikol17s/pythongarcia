from os import strerror

def nuevoArchivo(NombreArchivo):
    try:
        archivo = open(NombreArchivo)
        print('El archivo ya existe.')
        lineas = archivo.readlines()
        numLineas = len(lineas)
        print(f'En el archivo hay {numLineas} lineas.')
        archivo.close()
    except FileNotFoundError:
        print('El archivo no existe.')
        try:
            archivo = open(NombreArchivo, "w")
            print(f'Archivo creado con exito: {NombreArchivo}')
            archivo.close()
        except IOError as e:
            print(f'Hay un error de: {strerror(e.errno)}')

nombre_archivo = 'Archivo.txt'
nuevoArchivo(nombre_archivo)