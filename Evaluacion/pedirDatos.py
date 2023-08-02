def solicitar_datos(NombreArchivo, datos):
    try:
        archivo = open(NombreArchivo, "a")
        for dato in datos:
            archivo.write(dato + '\n')
        archivo.close()
        print('Los datos se agregaron correctamente.')
    except Exception as e:
        print(f'Ha ocurrido un error: {e}')
    
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
num_cel = input('Ingrese su numero de celular: ')
datos = [nombre, apellido, num_cel]

solicitar_datos('Archivo.txt', datos)