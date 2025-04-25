import time

palabra=input("Ingrese una frase")
cont=0
vocales=0
cons=0
for i in palabra.lower():
    cont=cont+1
    print(cont, i)
    # time.sleep(1)
    if i in "aeiou":
        # vocales=vocales+1
        vocales+=1
    else:
        cons+=1
print("La cantidad de caracteres son ", cont)
print("La cantidad de vocales son ", vocales)
print("La cantidad de consonantes son ", cons)