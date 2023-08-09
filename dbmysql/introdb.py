import mysql.connect

database = MYSQL.connect.connect(
    host='localhost',
    user='root',
    password='',
    database='proyecto_sena'
)

cursor = database.cursor()

def insertar_empresa():
    print('Datos a agregar a la tabla Empresa...')
    nit = input('NIT: ')
    nombre = input('Nombre Empresa: ').upper()
    email = input('Correo Electronico: ').lower()
    telefono = input('Numero De Telefono: ')
    direccion = input('Direccion De La Empresa: ').lower()
    tipo_empresa = input('Tipo Empresa (PUBLICA - PRIVADA - MIXTA): ').lower()
    num_trabajadores = input('Numero Trabajadores: ')

    consulta = 'INSERT INTO empresas (nit, nombre, email, telefono, direccion, tipo_empresa, num_trabajadores) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    valores = (nit, nombre, email, telefono, direccion, tipo_empresa, num_trabajadores)

    cursor.execute(consulta, valores)
    database.commit()

    print('Empresa creada con exito.')

insertar_empresa()

def Consultar():
        valor = input('Ingrese el campo a consultar:')
        consultar = f"SELECT {valor} FROM candidato;"
        print(consultar)

        cursor = database.cursor()
        cursor.execute(consulta)
        for dato in cursor:
            print(dato)
        cursor.close()

def actualizar_empresa():
        c1 = input('Ingrese el nombre del campo actual:')
        d1 = input('Ingrese el dato nuevo del campo que eligió:')
        c2 = input('Ingrese un campo relacionado con el dato a cambiar:')
        d2 = input('Ingrese el dato del campo relacionado que eligió:')
        
        ModificarRegistro = f"UPDATE candidato SET {c1} = %s WHERE {c2} = %s;"
        print(ModificarRegistro)

        cursor = database.cursor()
        cursor.execute(mfcarRegistro, (d1, d2))
        database.commit()
        cursor.close()

def eliminarDatos():
        cam = input('Ingrese el campo a consultar:')
        dato = input('Ingrese el dato a eliminar:')
        eliminar = f"DELETE FROM candidato WHERE {campo} = %s;"
        print(eliminar)

        cursor = database.cursor()
        cursor.execute(eliminar, (dato,))
        database.commit()
        cursor.close()
