from Cliente import *
class Compañia(Cliente):
    def __init__(self,nombre,telefono,correo,tipo):
        super().__init__(nombre,telefono,correo,tipo)
        self.__nombre=nombre
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    
