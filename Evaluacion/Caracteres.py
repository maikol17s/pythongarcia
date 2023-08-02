def Caracteres(nombreArchivo):
    try:
        archivo = open(nombreArchivo, 'r')
        contenido = archivo.read()
        numCaracteres = len(contenido)
        archivo.close()
        print(f'El archivo tiene {numCaracteres} caracteres.')
    except FileNotFoundError:
        print(f'El archivo {NombreArchivo} no existe.')

nombreArchivo = 'Archivo.txt'
Caracteres(nombreArchivo)