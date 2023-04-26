x=int(input('ingrese numero: '))
y=int(input('ingrese numero: '))            # definición de variables.
z=int(input('ingrese numero: '))
#indentación
if x>y:           #incio de las condiciones, si no se cumplen, pasara al primer else.

    if x>z:       #Esta condicion no se va a cumplir si la primer condición no se cumple.
        print(f'el mayor es {x}')          
    else:         #si la condición anterior no se cumples esta si se cumplirá.
        print(f'el mayor es {z}')
else:             #esta condición se cumplirá si el primer if no se cumple.
    if y>z:
        print(f'el mayor es {y}')
    else:         # esta condicon se cumple si la anterior condicion (if) no se cumple y termina el programa
        print(f'el mayor es {z}')
