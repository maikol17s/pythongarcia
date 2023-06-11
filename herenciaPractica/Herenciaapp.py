from Individual import *
from Compañia import *
from Producto import *

c1=Individual('Daniel','Jimenez',21432,32045321,'dani@gmail.com','natural')
p1=Producto('Caja de tijeras',150000,3.5)
p2=Producto('Caja de lapiz',20000,3.5)
print(c1.getdatos())
c1.agregarProducto(p1)
c1.agregarProducto(p2)
c1.componerProducto('Reglas',12,2000,3.5)
for producto in c1.getNue_producto():
    print(producto.getNombre())
print(p1.getdatos())
print(p2.getdatos())
print(f'La rebaja es de: {p1.Rebaja()}')
print(f'La rebaja es de: {p2.Rebaja()}')

print()

c2=Compañia('chocoleit',99910022,'choco@gmail.com','industrial')
l1=Producto('Cuadernos',500000,2)
l2=Producto('Carpetas',250000,2)
print(c2.getdatos())
c2.agregarProducto(l1)
c2.agregarProducto(l2)
c2.componerProducto('Resmas',1,300000,2)
for producto in c2.getNue_producto():
    print(producto.getNombre())
print(l1.getdatos())
print(l2.getdatos())
print(f'La rebaja es de: {l1.Rebaja()}')
print(f'La rebaja es de: {l2.Rebaja()}')
