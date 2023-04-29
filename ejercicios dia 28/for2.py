#Ejercicio 14
for i in range (100, 500):
    num=i
    u=num%10
    num=num//10
    d=num%10
    c=num//10
    print(c, d, u)
    cubo=(c**3)+(d**3)+(u**3)
    if cubo == i:
        print("ES VALIDO")
    else:
        print("No es valido")