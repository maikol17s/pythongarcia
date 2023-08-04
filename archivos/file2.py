#Escriba un programa que diga cuantas letras tiene el coro del himno de soacha
#Escriba la respuesta en otro archivo 

#escriba un progrma que diga cuantas letras tine cada linea del coro del himno de shoacha 
#escriba la respuesta en otro archivo

#escriba un progrma que diga cuantas letras tiene cada linea del coro del himno de shoacha 
#escriba la respuesta en otro archivo

try:

    with open("Archivos/intro.txt", "r", encoding="utf-8") as file:
        linea = file.readlines()
        numLineas = len(linea)
        print("El número de líneas es:", numLineas)

   
    with open("Archivos/intro.txt", "r", encoding="utf-8") as file:
        cont = 1
        with open("Archivos/intro1.txt", "w", encoding="utf-8") as archivo:
            for line in file:
                numCaracteres = len(line.strip())
                print(f"La línea {cont} tiene {numCaracteres} caracteres")
                cont += 1
                archivo.write(f"La línea {cont} tiene {numCaracteres} caracteres\n")

except IOError as e:
    print(e)
