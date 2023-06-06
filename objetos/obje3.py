class empleado:
    cont = 0
    suma_Salarios = 0

    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        empleado.cont +=1
        empleado.suma_Salarios += self.__salario

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    
    def salarioHora(self,horas_trab):
        salario_hora=self.__salario / horas_trab
        return salario_hora
    
    def incremento(self):
        if self.__salario > 1160000:
            ipc = self.__salario * 13.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc
        else:
            ipc = self.__salario * 16.12 / 100
            incremento = self.__salario + ipc
            self.__salario = incremento
            return ipc
    def  horasExtras(self, horas):
        if horas > 40:
            return f"No se admiten mas de 2 horas diarias"
        else:
            suma = 4833 * horas
            self.__salario = self.__salario + suma
            return suma

    def getSuma(self):
        return p.suma_Salarios
    
    def prome_Salarios(self):
        promSalarios = p.suma_Salarios / empleado.cont
        return promSalarios

    def getdatos(self):
         return f'{self.__nombre}, {self.__cargo},{self.__salario}'


p=empleado('Ana','secretario',1000000)
print(p.getNombre())
print(p.getCargo())
print()
horas_trab=int(input('Ingrese horas trabajadas: '))
salario_hora= p.salarioHora(horas_trab)
print(f'El empleado {p.getNombre()} gana {salario_hora:.2f} por hora')
print()
print(f'El incremeto es de: {p.incremento()}')
print(p.horasExtras(9))
print(f'La suma de los salarios es: {p.getSuma()}')
print(f'El promedio de los salarios es de: {p.prome_Salarios()}')
print(p.getdatos())

print()

q=empleado('Pedro','ejecutivo',2000000)
print(q.getNombre())
print(q.getCargo())
print()
horas_trab=int(input('Ingrese horas trabajadas: '))
salario_hora= q.salarioHora(horas_trab)
print(f'El empleado {q.getNombre()} gana {salario_hora:.2f} por hora')
print()
print(f'El incremeto es de: {q.incremento()}')
print(q.horasExtras(9))
print(f'La suma de los salarios es: {q.getSuma()}')
print(f'El promedio de los salarios es de: {q.prome_Salarios()}')
print(q.getdatos())
