class persona:
    def __init__(self, nombre, documento,cursos):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=cursos

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento
    
    def agregarCursos(self, curso):
        while curso !="fin":
            self.__curso.append(cursos)
    def getCurso(self):
        return self.__cursos

    def getDatos(self):
        return f'{self.__nombre}, {self.__documento},{self.__cursos}'

p=persona('Ana',123,2)
print(p.getNombre())
q=persona('Ronald',321,5)
print(q.getNombre())

p.setNombre('Maria')
print(p.getNombre())
q.setNombre('Jhon')
print(q.getNombre())

p.getDatos()
print(p.getDatos())
q.getDatos()
print(q.getDatos())