compra=float(input("Ingresar valor de la compra: "))

if compra >= 50000:
    print("Su descuneto es de 20%")
    total= compra * .20
    print(total)
else:
    print("No tiene descuento")
