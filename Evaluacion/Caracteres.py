def Caracteres(NombreArchivo):
    try:
        archivo = open(NombreArchivo, 'r')
        contenido = archivo.read()
        numCaracteres = len(contenido)
        archivo.close()
        print(f'El archivo contiene {numCaracteres} caracteres.')
    except FileNotFoundError:
        print(f'El archivo {NombreArchivo} no existe.')

nombreArchivo = 'Archivo.txt'
Caracteres(nombreArchivo)