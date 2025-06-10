# Uso y manejo de numeross
# que es una numeros?
# es una coleccion de datos

#     -6- 5 -4 -3  -2  -1
numeros=[3, 6, 2, 88, 45, 5]
#      0  1  2  3   4   5

# print(numeros)
# # print(numeros.index(88))
# numeros.append(64)

# print(numeros)

# for numero in numeros:
#     print("notas:" ,numero*3)

# num=int(input("Ingrese un numero: "))

# numeros.append(num)

# print(numeros)

nombre=["Arthur", "Leon", "Nathan"]
apellidos=["Morgan", "Kennedy", "Drake"]
while True:
    print('''
        1.- Ingresar nombre
        2.- Buscar Nombre
        3.- Mostrar lista
        4.- Salir
          ''')
    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            nom=input("Ingrese un nombre: ")
            nombre.append(nom)
            print(nombre)
            ape=input("Ingrese un apellido: ")
            nombre.append(ape)
            print(apellidos)
        case 2:
            busca=input("Ingrese el nombre a buscar: ")
            if busca in nombre:
                print(f"El nombre {busca} si existe en la lista")
            else:
                print(f"El nombre {busca} no existe en la lista")
        case 3:
            # cont=0
            # for n in nombre:
            #     print(cont+1, ".-", nombre[cont], "", apellidos[cont])
            #     cont+=1
            for i in range(len(nombre)):
                print(i+1, ".-", nombre[i], apellidos[i])
        case 4:
            print("Saliendo....")
            break
        case _:
            print("Opcion no valida")
