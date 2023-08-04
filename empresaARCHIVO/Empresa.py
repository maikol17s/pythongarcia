class empresa:
    def __init__(self,nitEmpresa,contrato,fechaInicio,fechaCierre):
        self.__nitEmpresa=nitEmpresa
        self.__contrato=contrato
        self.__fechaInicio=fechaInicio
        self.__fechaCierre=fechaCierre
    
    def getnitEmpresas(self):
        return self.__nitEmpresa
    
    def getContratos(self):
        return self.__contrato
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaCierre(self):
        return self.__fechaCierre


    def getverDatos(self):
        return f'{self.__nitEmpresa},{self.__contrato},{self.__fechaInicio},{self.__fechaCierre}'