class persona:
    def __init__(self, nombre, documento):
        self.__nombre=nombre
        self.__documento=documento
    def __init__(self, cursos):
        self.__cursos=[]

    def subirCursos(self, curso):
        self.__curso += [curso]

    def getCursos(self):
        return self.__curso

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento

    def getDatos(self):
        return f'{self.__nombre}, {self.__documento}'


p=persona('Ana',123)
print(p.getCursos())
p.subirCursos(101)
p.subirCursos(501)
p.subirCursos(301)
q=persona('Ronald',321)
print(q.getCursos())


p.setNombre('Maria')
print(p.getNombre())
q.setNombre('Jhon')
print(q.getNombre())


p.getDatos()
print(p.getDatos())
q.getDatos()
print(q.getDatos())