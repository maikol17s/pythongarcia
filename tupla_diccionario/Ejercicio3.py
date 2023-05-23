#Ejercicio 3

d1 = {"leon": "lion", "elefante": "elephant", "sapo": "toad","tortuga": "tortoise"}

def tuanimal1(d1):
    l1=[]
    l2=[]
    for clave,valor in d1.items():
        l1.append({clave})
        l2.append({valor})
        tuplaEs = tuple(l1)
        tuplaIn = tuple(l2)
    return (tuplaEs, tuplaIn)
  
tuplaA, tuplaB= tuanimal1(d1)
print ("La tupla en español son: ", tuplaA)
print ("La tupla en ingles son: ", tuplaB)
