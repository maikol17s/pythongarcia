
from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}


numeros_counter = 0
caracteres_counter = 0
caracteres_especiales = "{[/<¡(`^)%;>'}-@#$*,_!+|¿:].?"
file_name = input("Ingresa el nombre del archivo a analizar: ")


try:
    with open(file_name, "rt") as file:
        for line in file:
            for char in line:
                if char.isalpha():
                    counters[char.lower()] += 1
                elif char.isdigit():
                    numeros_counter += 1
                elif char in caracteres_especiales:
                    caracteres_counter += 1
        file.close()

    for char, count in counters.items():
        if count > 0:
            print(char, '->', count)

    
    print(f'Caracteres numericos -> {numeros_counter}')
    print(f'Caracteres especiales -> {caracteres_counter}')

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
