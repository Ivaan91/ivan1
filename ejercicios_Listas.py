#validar con manejo de excepciones  ! 
from os import system
"""
ejercicio

menu de opciones 
1.- agregar elemento a la lista
2.- eliminar elemento de la lista
3.- mostrar cada uno de los elemento de la lista de forma ordenada
4.- cerrar sistema

"""
system("cls")
lista_productos = ["a","b","c"]
while True:
    print("Menú de Listas")
    print("1.- agregar elemento a la lista")
    print("2.- eliminar elemento de la lista")
    print("3.- mostrar cada uno de los elemento de la lista de forma ordenada")
    print("4.- cerrar sistema")
    opc = int(input("→ ")) #debería validar con try except 
    match opc:
        case 1 :
            nombre_producto = input("ingrese producto : ")
            lista_productos.append(nombre_producto)
            input("presione enter para continuar ! ")
            system("cls")
        case 2 :
            cont = 1
            for i in lista_productos:
                print(f"{cont}.-{i}")
                cont += 1
            aux = int(input("cual desea eliminar → "))-1 #debe ser validado
            lista_productos.pop(aux)
            input("presione enter para continuar ! ")
            system("cls")
        case 3 : 
            cont = 1
            for i in lista_productos:
                print(f"{cont}.-{i}")
                cont += 1
            input("presione enter para continuar ! ")
            system("cls")
        case 4 : 
            
            print("saliendo del sistema")
            input("presione enter para continuar ! ")
            system("cls")
            break
        case _ :
            print("ingreso otro valor ! ")
            input("presione enter para continuar ! ")
            system("cls")