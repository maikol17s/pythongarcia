import mysql.connect

database = mysql.connector.connect(
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