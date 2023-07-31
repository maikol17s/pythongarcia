from os import strerror

def buscarArchivo(nombreArchivo):
    try:
        file = open(nombreArchivo)
        print("El archivo ya exite")
        linea=file.readlines()
        numLineas=len(linea)
        print(f'El archivo tiene {numLineas} lineas')
        file.close()
    except FileNotFoundError:
        print("El archivo no exite")
        try:
            file= open (nombreArchivo,"w")
            print("Archivo creado con exito")
        except:
            print(f'Ocurrio un  error')
        try:
            with open ('Archivo2.txt',"w+"):
                nombreArchivo.write('\n' + 'Hola mundo')
                nombreArchivo.close()
            except IOError as e:
            print(f'Ocurrio un error: {strerror(e.errno)}')

nombreArchivo=('C:\garcia\pythongarcia\Evaluacion\Archivo2.txt')
print(buscarArchivo(nombreArchivo))


