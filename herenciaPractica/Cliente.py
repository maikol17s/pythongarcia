from Producto import*
class Cliente:
    def __init__(self,nombre,telefono,correo,tipo):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__correo=correo
        self.__tipo=tipo
        self.__producto=[]
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getTelefono(self,telefono):
        return self.__telefono
    def setTelefono(self):
        self.__telefono=telefono
    
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo=correo
    
    def getTipo(self):
        return self.__tipo
    def setTipo(self,tipo):
        self.__tipo=tipo
    
    def agregarProducto(self,producto):
        self.__producto.append(producto)
    def componerProducto(self,nombre,id,precio,descuento):
        pro=Producto(nombre,precio,descuento)
        self.__producto.append(pro)
    def getNue_producto(self):
        return self.__producto
    
    def getdatos(self):
         return f'{self.__nombre}, {self.__apellido},{self.__documento},{self.__telefono},{self.__correo},{self.__tipo}'
    
    def getdatos(self):
         return f'{self.__nombre},{self.__telefono},{self.__correo},{self.__tipo}'
    
    