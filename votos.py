guaripolo=0
tulio=0

cant=int(input("Ingrese el numeros de votantes"))
for i in range(cant):
    print('''
          Ingrese su voto:
          1.- Guaripolo
          2.- Tulio 
          ''')
    voto=int(input())
    if voto==1:
        guaripolo=guaripolo+1
    elif voto==2:
        tulio=tulio+1
    else:
        print("Ingrese una opcion valida")
print("Los votos de Guaripolo son: ", guaripolo)
print("Los votos de Tulio son: ", tulio)
if guaripolo>tulio:
    print("Gano Guaripolo")
else:
    print("Gano Tulio")




