from Alumno import *
import csv
alumnos=[]
with open ('C:\Users\SENA\Downloads') as prueba:
    csvReader=csv.reader(prueba)
    for row in csvReader:
        objeto=alumno(row[0],row[1],row[2],row[3])
        print(objeto.verDatos())
        alumnos.append(objeto)
