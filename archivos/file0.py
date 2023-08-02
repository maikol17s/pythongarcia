try: 
    file=open('archivos/intro.txt','r',encoding='utf-8')
    cont=0
    for linea in file:
        file.readline()
        print(f'{cont} {file}')
        cont+=1
        file.close()
except IOError as e:
    print(e,'...')