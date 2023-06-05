class persona:
    def __init__(self, nombre, documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__cursos=[]

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
    
    def subirCursos(self, curso):
        self.__curso += [curso]

    def getCursos(self):
        return self.__curso
    
    def buscarCurso(self, curso):
        if curso in self.__curso:
            return f"El {curso} esta en la lista."
        else:
            return f"El{curso} no esta en la lista de cursos."
        
    

p=persona('mario',3001)
print(p.getNombre())
print(p.getCursos())
print(p.subirCursos(101))
print(p.subirCursos(301))
print(p.subirCursos(201))
print(p.subirCursos(601))
print(p.getDatos())
p=persona('mario',3001)
print(p.getNombre())
print(p.getDocumento)
print(p.buscarCurso(601))
print(p.buscarCurso(202))
print(p.getDatos())
