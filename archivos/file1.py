try:
    stream=open('archivos/intro.txt','r',encoding='utd-8')
    #print(stream.reallines())
    for linea in stream.readlines():
        print(linea)
except IOError as e:
    print(e,'...')