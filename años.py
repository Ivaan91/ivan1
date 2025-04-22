edad=int(input("Ingrese su edad "))

if edad<12:
    print("Es un niño")
elif edad>=12 and edad<=17:
    print("Es adolescente ")
elif edad>=18 and edad<=64:
    print("Es audlto")
else:
    print("Es adulto mayor")