class cliente:
    def __init__(self,tipo):
        self.__tipo=tipo 
    
    def getTipo(self):
        return self.__tipo
    def setTipo(self,tipo):
        self.__tipo=tipo