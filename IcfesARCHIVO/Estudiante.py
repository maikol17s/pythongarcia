class Estudiante:
    def __init__(self,tipoDoc,estrato, puntNatu, puntSoc):
        self.__tipoDoc=tipoDoc
        self.__estrato =self.entero(estrato)
        self.__puntNatu =self.entero(puntNatu)
        self.__puntSoc = self.entero(puntSoc)
    
    def entero(self, valor):
        try:
            return int(valor)
        except ValueError:
            return 0

    def getTipoDoc(self):
        return self.__tipoDoc
    def getEstrato(self):
        return self.__estrato
    def getPuntNatu(self):
        return self.__puntNatu
    def getPuntSociales(self):
        return self.__puntSoc

    def verDatos(self):
        return f'{self.__tipoDoc}{self.__estrato},{self.__puntNatu},{self.__puntSoc}'

