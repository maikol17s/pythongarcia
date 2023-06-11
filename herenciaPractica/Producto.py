class Producto():
    rebaja=0
    def __init__(self,nombre,precio,descuento):
        self.__nombre=nombre
        self.__precio=precio
        self.__descuento=descuento
        Producto.rebaja
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getPrecio(self):
        return self.__precio
    def setPrecio(self,precio):
        self.__precio=precio
    
    def getDescuento(self):
        return  self.__descuento
    def setDescuento(self,descuento):
        self.__descuento=descuento
    
    def Rebaja(self):
        rebaja=self.__precio * self.__descuento // 100
        return rebaja
    
    def getdatos(self):
        return f'{self.__nombre},{self.__precio},{self.__descuento}'