from os import strerror

f1 = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 2)}
f2= input("Ingresa el nombre del archivo a analizar: ")
try:
    file = open(f2, "rt")
    for line in file:
        for char in line:
            if char.isalpha():
                f1[char.lower()] += 1
    file.close()
    for char in f1.keys():
        b = f1[char]
        if b > 0:
            print(char, '->', b)
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))