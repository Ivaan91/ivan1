# Explicacion y uso de for
# todos los indices en python comienzan en 0

# num=int(input("Ingrese un numero "))
# for i in range(num)
# print(i)

# num=9
# for i in range(10):
# print(num,"x",i+1,"=", (i+1)*num)

cant=int(input("Ingrese el numeros de notas6"))
suma=0
for i in range(cant):
    print("Ingrese la nota", i+1)
    nota=float(input())
    suma=suma+nota
prom=suma/cant
print("El promedio es ",round(prom,1))

if prom<4:
    print("Usted reprobo")
else:
    print("Usted aprobo")
