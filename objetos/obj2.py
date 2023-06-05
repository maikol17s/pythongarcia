class Persona:
    cursosGeneral = ['Php','Java']

    def __init__(self, nombre, documento):
        self.__nombre = nombre
        self.__documento = documento
        self.__cursos = []

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getDocumento(self):
        return self.__documento

    def setDocumento(self, documento):
        self.__documento = documento

    def agregarCursos(self, curso):
        self.__cursos.append(curso)
        self.agregarCurso(curso)

    def agregarCurso(self, curso):
        if curso not in Persona.cursosGeneral:
            Persona.cursosGeneral.append(curso)

    def getCursos(self):
        return self.__cursos

    def getdatos(self):
        return f'{self.__nombre}, {self.__documento}, {self.__cursos}'


p = Persona('Ana', 1234)
print(p.getNombre())
print(p.getDocumento())
p.agregarCursos('Python')
print(p.getCursos())
print(Persona.cursosGeneral)
print(p.getdatos())