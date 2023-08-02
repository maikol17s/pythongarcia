#Escriba un programa que diga cuantas letras tiene el coro del himno de soacha
#Escriba la respuesta en otro archivo 

#escriba un progrma que diga cuantas letras tine cada linea del coro del himno de shoacha 
#escriba la respuesta en otro archivo

try:
        file = open("archivos/intro.txt", "r", encoding= "utf-8")
        file1 = open("archivos/intro.txt", "r")
        contenido = file1.read()
        numCaracteres = len(contenido)        
        cont = 1
        archivo = open("archivos/intro1.txt", "a", encoding= "utf-8")
        for line in archivo:
            file1.readline()
            print(f"{line} {numCaracteres}")
            cont +=1
            archivo.write (file1 + "\n") 
        file.close()

            
except IOError as e:
    print (e)