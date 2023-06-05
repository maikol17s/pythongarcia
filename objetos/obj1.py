class persona:
    def __init__(self, nombre, documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__curso=[]

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getDocumento(self):
        return self.__documento
    def setDocumento(self,documento):
        self.__documento=documento
    
    def agregarCurso(self, curso):
        self.__curso.append(curso)

    def getCursos(self):
        return self.__curso

    def getDatos(self):
        return f'{self.__nombre}, {self.__documento},{self.__curso}'

p=persona('Ana',123)
print(p.getNombre())
q=persona('Ronald',321)
print(q.getNombre())

p.agregarCurso('Matematicas')
print(p.getCursos())
q.agregarCurso('Ingles')
print(q.getCursos())

p.setNombre('Maria')
print(p.getNombre())
q.setNombre('Jhon')
print(q.getNombre())

p.getDatos()

print(p.getDatos())
q.getDatos()
print(q.getDatos())