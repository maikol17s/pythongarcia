class alumno:
    def __init__(self,codigoIcfes,fechaNacimiento,codigoDane,codigoColegio):
        self.codigoIcfes=codigoIcfes
        self.fechaNacimiento=fechaNacimiento
        self.codigoDane=codigoDane
        self.codigoColegio=codigoColegio

    def verDatos(self):
        return f'{self.codigoIcfes},{self.fechaNacimiento},{self.codigoDane},{self.codigoColegio}'