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

my_tuple = (11, 104, 10, 1000) 
#print(#sort(my_tuple))
#my_tuple.append(10000)
my_tuple=my_tuple+(100,)
#del my_tuple[0]
#my_tuple[1] = -10
print(my_tuple)
print(len(my_tuple))
print(my_tuple+my_tuple)
print(my_tuple*3)

var = 123
t1 = (1,1,1,1,1,)
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

tam=random.randint(5,15)
t=()
for i in range(tam):
    n=random.randrange(100)
    t+=(n,)

print(t)
