class Cursos:
    def __init__(self):
        self.__curso = []

    def agregarCurso(self, curso):
        self.__curso.append(curso)

    def getCursos(self):
        return self.__curso

    def eliminarCurso(self, curso):
        if curso in self.__curso:
            self.__curso.remove(curso)
        else:
            print('El curso no está en la lista.')

    def modificarCurso(self, curso, n_curso):
        Cont = 0
        for x in range(len(self.__curso)):
            Cont+=1
            if self.__curso[x] == curso:
                self.__curso[Cont-1] = n_curso
            if self.__curso[x] == self.__curso[-1]:
                self.__curso[-1] = n_curso

    def buscarCurso(self, curso):
        if curso in self.__curso:
            print(f'El curso {curso} está en la lista.')
        else:
            print(f'El curso {curso} no está en la lista.')

    def consultarCurso(self, posicion):
        if 0 <= posicion < len(self.__curso):
            print(f'En la posicion {posicion} esta el curso {self.__curso}')
        else:
            print(f'La posicion {posicion} no existe. ')

p = Cursos()

#Agregar un curso.
p.agregarCurso('Matematicas')
print(p.getCursos())

#Eliminar un curso.
p.eliminarCurso('Matematicas')
print(p.getCursos())

#Modificar un curso.
p.agregarCurso('Matematicas')
print(p.getCursos())
p.modificarCurso('Matematicas', 'Ingles')
print(p.getCursos())

#Buscar un curso.
p.buscarCurso('Ingles')
p.buscarCurso('Fisica')

#Consultar un curso por su posicion.
p.consultarCurso(0)