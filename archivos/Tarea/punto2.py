#Desarrollar el ejemplo de hoy con with open
def Caracteres(nombreArchivo):
    try:
        with open(nombreArchivo, 'r') as archivo:
            contenido = archivo.read()
            numCaracteres = len(contenido)
            archivo.close()
            print(f'El archivo contiene {numCaracteres} caracteres.')
    except FileNotFoundError:
        print(f'El archivo {nombreArchivo} no existe.')

nombreArchivo = 'Archivo.txt'
Caracteres(nombreArchivo)