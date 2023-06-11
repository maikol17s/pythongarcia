from Cliente import *
class Individual(Cliente):
    def __init__(self,nombre,apellido,documento,telefono,correo,tipo):
        super().__init__(nombre,telefono,correo,tipo)
        self.__apellido=apellido
        self.__documento=documento

    def getApellido(self):
        return self.__apellido
    def setApellido(self,apellido):
        self.__apellido=apellido
    
    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento
    

