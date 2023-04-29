import random

secreto = random.randint(1, 100)
acertado=  False

while not acertado:
    num = int(input('Adivine el numero: '))
    if num == secreto:
        print('Acertastes el numero, Felicidades ')
        acertado == True
    elif num < secreto:
        print('El numero secreto es mayor')
    else:
        print('El numero secreto es menor ')




