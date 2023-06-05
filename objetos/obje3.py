class empleado:
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario

    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getCargo(self):
        return self.__cargo
    def setCargo(self,cargo):
        self.__cargo=cargo
    
    def salario(salariomen,horastrab):
        salariomen=int(input('Ingrese salario: '))
        horastrab=int(input('Ingrese horas trabajadas: '))
        salariohora=salariomen / (horastrab)
        return salariohora
    
    def getsalario(self):
        return self.__salario
    
    def getdatos(self):
        return f'{self.__nombre}, {self.__cargo}'


p=empleado('Ana','secretario')
print(p.getNombre())
print(p.getCargo())
p.getsalario()
print(p.getsalario())
print(p.getdatos())
