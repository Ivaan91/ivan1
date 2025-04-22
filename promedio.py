# sacar el promedio de 3 numeros


print("Ingrese 3 numeros")
n1=int(input())
n2=int(input())
n3=int(input())
prom=(n1+n2+n3)/3
print("Su promedio es", round(prom,2))

if prom<40:
    print("Usted reprobo")
else:
    print("Usted aprobo")
