calif1=int(input("Ingrese primera calificacion: "))
calif2=int(input("Ingrese segunda calificacion: "))
calif3=int(input("Ingrese tercera calificacion: "))

nota= (calif1 + calif2 + calif3)

if nota >= 70:
    print("Alumno Aprobado")
    print(nota)
else:
    print("Alumno Reprobado")
    print(nota)