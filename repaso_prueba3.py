# nuevos diccionarios y manipulacion de datos


juegos={
    1:{
        "nombre": "Metroid Dread",
        "precio": 50000,
        "code":"MMdd23"
    },
    2:{
        "nombre": "Pinkmin 4",
        "precio": 55000,
        "code":"pKMn2022"
    }
}
# nombre=input("Ingrese el nombre del juego: ")
# precio=int(input("Ingrese el precio: "))
# code=input("Ingrese el codigo: ")

# juegos[4]={
#         "nombre": nombre,
#         "precio": precio,
#         "code":code
# }

# for j, datos in juegos.items():
#     print(j, datos)

'''
El codigo debe tener 2 mayusculas
y 2 minusculas

'''
def mostrar_juegos(dic):
    for j, datos in juegos.items():
        print(j, datos)
def act_juegos(dic):
    mostrar_juegos(dic)
    act=int(input("Seleccione el juegos a actualizar: "))
while True:
    try:
        print('''
              1.- Agregar juego
              2.- Mostar juego
              3.- Actualizar juego
              4.- Borrar juego
              5.- Salir
            ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                nombre=input("Ingrese el nombre del juego: ")
                precio=int(input("Ingrese el precio: "))
                code=input("Ingrese el codigo: ")
                largo=len(juegos)
                juegos[largo+1]={
                        "nombre": nombre,
                        "precio": precio,
                        "code":code
                    }
            case 2:
                mostrar_juegos(juegos)
            case 3:
            case 4:
                mostrar_juegos(juegos)
                borrar=int(input("Cual juego desea borrar?"))
                del juegos[borrar]
            case 5:
                break
            case _:
                print("Opcion ivalida")
    except Exception:
