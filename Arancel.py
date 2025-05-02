
arancel=200000
descuento=0
print(''' 
      1.- La Florida 20%
      2.- La Pintana 30%
      3.- Puente Alto 25%
      4.- San Joaquin 15%
       ''')
comuna=int(input("Seleccione una comuna: "))

if comuna==1:
    descuento=20
elif comuna==2:
    descuento=20
elif comuna==3:
    descuento=25
elif comuna==4:
    descuento=15
else:
    print("Seleccion incorrecta")

grupo=int(input("Ingrese su grupo familiar (incluido usted): "))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo>=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else:
    print("Seleccion incorrecta")

print("El descuento total es ", descuento)
desc=arancel*descuento/100
total=arancel-desc
print("El total a pagar es $", total)