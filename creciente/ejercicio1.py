import random
lon = random.randrange(200, 2500)
def llenarLista(tamaño):
    lista=[]
    lista=[random.randint(100, 500) for i in range(tamaño)]
    return lista

listado = llenarLista(lon)
print(listado)

# listado = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def ordenAsc(lista):
    for j in range(len(lista)):
        for g in range(j +1, len(lista)):
            if lista[j] >  lista[g]:
                aux=lista[j]
                lista[j]=lista[g]
                lista[g]=aux
    return f"la lista ordenada en orden ascendente: {lista}"

print(ordenAsc(listado))

def cuartil(lista):
    formula=0
    n = len(lista)
    listaCuartil=[]
    conv=0
    # posicionInicial=0
    for k in range(1, 4):
        if len(lista) % 2!=0:
            # posicionInicial=conv
            formula=(k*(n+1)) / 4
            conv=round(formula)
            pos=lista[conv-1]
            print(f"Q{k} = posicion {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
            # if k == 1:
            #     listaCuartil=lista[ :conv-1]
            #     listaCuartil.append(formula)
            #     print(f"Cuartil {k} {listaCuartil}")
            # elif k == 2:
            #     listaCuartil = lista[posicionInicial-1:conv]
            #     print(f"Cuartil {k} {listaCuartil}")
            # else:
            #     listaCuartil = lista[posicionInicial:conv]
            #     print(f"Cuartil {k} {listaCuartil}")
        else:
            formula = (k*n)/4
            conv=round(formula)
            pos= lista[conv]
            print(f"Q{k} = {formula} en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
            
    return "Fin de procedimiento de cuartiles"
            
print(cuartil(listado))

def quintil(lista):
    formula=0
    n = len(lista)
    listaCuartil=[]
    conv=0
    # posicionInicial=0
    for k in range(1, 5):
        if len(lista) % 2!=0:
            # posicionInicial=conv
            formula=(k*(n+1)) / 5
            conv=round(formula)
            pos=lista[conv-1]
            print(f"k{k} = posicion {formula} valor en lista {pos}")
            listaCuartil.append(formula)
            print(listaCuartil)
        else:
            formula = (k*n)/5
            conv=round(formula)
            print(f"k{k} = {formula}")
            listaCuartil.append(formula)
            print(listaCuartil)

    return "Fin de procedimiento de quintiles"
print(quintil(listado))

print()

def sumalista(lista):
    sum=0
    for i in cuartil(listado):
        sum+=i
    return sum
    

print('La suma del cuartil es: ',sumalista(cuartil))
print('La suma del quintil es: ',sumalista(quintil))

print()

def prolista(listado):
    return sumalista(cuartil)/len(listado)

def prolista2(l):
    return sumalista(quintil)/len(listado)

print('El promedio del cuartil es de: ',prolista(cuartil))
print('El promedio del quintil es de: ',prolista2(quintil))




    