import random

#tam = random.randint(5, 15)
#lista =[random.randrange (10,15) for i in range (tam)]
#t1=lista,
#print(t1)

tam=random.randint(5,15)
t=()
for i in range(tam):
    n=random.randrange(100)
    t+=(n,)

print(t)

t2=()
t3=()
t2=t[:5]
t3=t[5:]

print(t2)
print(t3)

print(type(t2))
print(type(t3))
