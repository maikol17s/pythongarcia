from Estudiante import *
import csv
estudiantes=[]

with open('archivos/IcfesARCHIVO/ICFES2019.csv','r') as prueba:
    csvReader=csv.reader(prueba)
    for row in csvReader:
        obj=Estudiante(row[0],row[14],row[66],row[69])
        estudiantes.append(obj)

def sumLis(lista):
    sum=0
    for x in lista:
        sum+=x
    return sum

def promLis(lista):
    return sumLis(lista)/len(lista)

def mayLis(lista):
    mayor=0
    for x in lista:
        if int(x) > mayor:
            mayor=x
    return mayor
        
def menLis(lista):
    menor=100000
    for x in lista:
        if x < menor:
            menor=x
    return menor
Documento=[f1.getTipoDoc() for f1 in estudiantes]
estratos=[f1.getEstrato() for f1 in estudiantes]
PuntoNatu=[f1.getPuntNatu()for f1 in estudiantes ]
PuntoSocia=[f1.getPuntSociales() for f1 in estudiantes ]

with open('archivos/IcfesArchivo/Resultados.txt', 'w') as resultado:
    resultado.write('Estrato mas alto es: '+ str(mayLis(estratos)) + '\n')
    resultado.write('Estrato mas bajo es: ' + str(menLis(estratos)) + '\n')

    resultado.write('Puntaje mas alto de  naturales es : ' + str(mayLis(PuntoNatu)) + '\n')
    resultado.write('Puntaje mas bajo de naturales es : ' + str(menLis(PuntoNatu)) + '\n')
    resultado.write ('Promedio de puntaje de naturales es: ' + str(promLis(PuntoNatu)) + '\n')

    resultado.write('Puntaje mas alto de sociales es: ' + str(mayLis(PuntoSocia)) + '\n')
    resultado.write('Puntaje mas bajo de sociales es: ' + str(menLis(PuntoSocia)) + '\n')
    resultado.write('Promedio de puntaje de sociales es: '+ str(promLis(PuntoSocia)) + '\n')
