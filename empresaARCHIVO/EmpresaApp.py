from Empresa import *
import csv
empresas=[]
with open('empresaArchivo/Contratos.csv','rt') as Archivo:
    Lectura=csv.reader(Archivo)
    for row in Lectura:
        objeto=empresa(row[1],row[0],row[2],row[5])
        print(objeto.getverDatos())
        empresas.append(objeto)
    
    
    def modaLista():
        cont=0
        rep=0
        moda=0
        for row in empresas:
                if moda == row:
                    cont+=1
                if cont > rep:
                    moda= i
        return moda
    
    def mediLista():
        mediana=(len(row[1]))
        if mediana % 2==0:
            medianaLista = (row[1][mediana//2-1]+row[0][mediana//2])/2
        else:
            medianaLista=row[1][mediana//2]
        return medianaLista
    
    with open ('empresaArchivo/Resultados.txt', 'w', encoding= 'utf-8') as archivoFinal:
        for f1 in empresas:
                print("NIT:', {f1.getnitEmpresas()}\n")
                print("contrato: , {f1.getContratos()}\n")
                print("fechaInicio: , {f1.getFechaInicio()}\n")
                print("fechaCierre: , {f1.getFechaCierre()}\n")


                archivoFinal.write(f"La moda de la lista es: {modaLista()}\n")
                archivoFinal.write(f"La mediana de la lista es: {mediLista()}\n")