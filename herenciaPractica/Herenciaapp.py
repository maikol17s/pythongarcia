from Individual import *
from Compañia import *
from Producto import *

c1=Individual('natural','Daniel' 'Jimenez',21432)
p1=producto('Caja de tijeras',12,150000)
p2=producto('Caja de lapiz',54,20000)
c1.agregarProducto(p1)
c1.agregarProducto(p2)
print(c1.getNue_producto())
c2=Compañia('foxfc',213322,'calle 21','fox@gmail.com','juridica',)
l1=producto('Caja de tijeras',12,150000)
l2=producto('Caja de lapiz',54,20000)
c2.agregarProducto1(l1)
c2.agregarProducto1(l2)
print(c2.getNue_producto())