frase=input("Frase: ")

print("Vocales en la frase:")

for x in "aeiou":
  if x in frase:
    print(x)