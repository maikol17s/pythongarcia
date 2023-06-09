from Cliente import *
from Producto import *
class Compañia(cliente):
    def __init__(self,nombre,telefono,direccion,correo,tipo):
        super().__init__(tipo)
        #super().__init__(nombre,id,precio)
        self.__nombre= nombre
        self.__telefono=telefono
        self.__direccion=direccion
        self.__correo=correo
        self.__nue_Producto1=[]

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getTelefono(self):
        return self.__telefono
    def setNombre(self, telefono):
        self.__telefono=telefono

    def getDireccion(self):
        return self.__direccion
    def setNombre(self, direccion):
        self.__direccion=direccion
    
    def getCorreo(self):
        return self.__correo
    def setCorreo(self, correo):
        self.__correo=correo
    
    def agregarProducto1(self,producto):
        self.__nue_Producto1.append(producto)
    
    def componerProducto1(self,nombre,id,precio):
        pro1=producto(nombre,id,precio)
        self.__nue_Producto1.append(pro1)
    
    def getNue_producto(self):
        return self.__nue_Producto1


