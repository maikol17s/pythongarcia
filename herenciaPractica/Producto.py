class producto ():
    def __init__(self,nombre,precio):
        self.__nombre=nombre
        self.__precio=precio
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getPrecio(self):
        return self.__precio
    def setPrecio(self,precio):
        self.__precio=precio
    