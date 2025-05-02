import random

#numAzar=random.randint(1,30)

#print(numAzar)

# dado=random.randint(1,6)
# print(dado)

numAdivinar=random.randint(1,50)

numAlea=int(input("Adivine el numero: "))

while numAlea!=numAdivinar:
    print(numAdivinar)
    if numAlea>numAdivinar:
        print("El numero es menor")
    else:
        print("El numero es mayor")
    numAlea=int(input("Adivine el numero: "))
print ("Le achuntaste")
