from Cliente import *
from Producto import *
class Individual(cliente):
    def __init__(self,tipo,nombre,apellido,documento):
        super().__init__(tipo)
        #super().__init__(nombre,precio)
        self.__nombre= nombre
        self.__apellido=apellido
        self.__documento=documento
        #self.__telefono=telefono
        # self.__direccion=direccion
        self.__nue_Producto=[]

    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getApellido(self):
        return self.__apellido
    def setNombre(self, apellido):
        self.__apellido=apellido

    def getDocumento(self):
        return self.__documento
    def setDocumento(self, documento):
        self.__documento= documento

    # def getTelefono(self):
    #     return self.__telefono
    # def setTelefono(self, telefono):
    #     self.__telefono=telefono

    # def getDireccion(self):
    #     return self.__direccion
    # def setNombre(self, direccion):
    #     self.__direccion=direccion
    
    def agregarProducto(self,producto):
        self.__nue_Producto.append(producto)
    
    def componerProducto(self,nombre,id,precio):
        pro=producto(nombre,id,precio)
        self.__nue_Producto.append(pro)
    
    def getNue_producto(self):
        return self.__nue_Producto

        

