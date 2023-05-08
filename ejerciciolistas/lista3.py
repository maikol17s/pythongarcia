num= int(input('Ingrese los digitos: '))

lista=[0,1]

while len(str(lista[-1])) < num:
    num2= lista[-1] + lista[-2]
    lista.append(num2)
print(lista)