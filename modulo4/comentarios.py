from os import strerror

# Inicializa 26 contadores para cada letra latina.

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}  # se crea un diccionario para contar cuantas veces aparcen las letras 
file_name = input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(file_name, "rt")   # se abre el archivo el lectura de texto 
    for line in file:              # itera en cada linea de mfile y lo guarda en line
        for char in line:          # itera en linea y lo guarda en char
            # Si es una letra...
            if char.isalpha():     # si es una letra devulve True si no False 
                # ... lo trataremos en minúsculas y actualizaremos el contador apropiado.
                counters[char.lower()] += 1 #se cambia a minuscula la letra y se incrementa en el contador en el diccionario para dicha letra
    file.close()                    # se cierra el archivo
    # Demos salida a los contadores.
    for char in counters.keys():     # secorre cada letra del diccionario
        c = counters[char]
        if c > 0:                    # si el valor de la letra es mayor a 0 se imprime la clave y el valor
            print(char, '->', c)
except IOError as e:                 #si ocurre un error al abrir el archivo se imprime un mensaje de error 
    print("Se produjo un error de E/S: ", strerror(e.errno))