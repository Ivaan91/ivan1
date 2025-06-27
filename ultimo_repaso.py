# Repasamos listas y diccionarios

# Perros de caza

perros={
    1:{"nombre": "Droopy",
       "raza": "Dog Hount",
       "codigo": "Dphh06"},
    2:{"nombre": "Spike",
       "raza": "Terrier",
       "codigo": "Strr07"}
}
#                    -1
# perros.keys() # [1, 4]
#
# list(perros.keys())[-1]

def mostrar_perros(dict):
    for key, perro in dict.items():
        print(key, perro)
def valida_pass(clave):
    Maysculas=False
    Minusculas=False
    Numero=False
    for palabra in clave:
        if palabra.isupper():
            Maysculas=True
        if palabra.islower():
            Minusculas=True
        if palabra.isdigit():
            Numero=True
    if Maysculas and Minusculas and Numero and len(clave)==6:
        print("La clave esta bien escrita")
        return True
    else:
        print("La clave esta mal escrita")
        return False
def ingres_perro(dict):
    nombre=input("Ingrese un nombre: ")
    raza=input("Ingrese una raza: ")
    codigo=input("Ingrese un codigo: ")
    if valida_pass(codigo):    
        largo=list(dict.keys())[-1]
        perros[largo+1]={"nombre": nombre,
                         "raza": raza,
                         "codigo": codigo}
    else:
        print("El parametro de la codigo no es correcto")
        print('''
               El codigo debe tener, una mayusculas, una minusculas, 
               un numero y un largo exacto de 6
                          ''')
def act_perros(dict):
    mostrar_perros(dict)
    act=int(input("Seleccione el perro a actualizar: "))
    while True:
        print('''
                1.- Nombre
                2.- Raza
                3.- Codigo
                4.- Salir
            ''')
        dato=int(input("Que dato va actualizar?: "))
        match dato:
            case 1:
                n=input("Ingrese el nuevo nombre: ")
                dict[act]["nombre"]=n
            case 2:
                n=input("Ingrese la nueva raza: ")
                dict[act]["raza"]=n
            case 3:
                n=input("Ingrese el nuevo codigo: ")
                if valida_pass(n):
                    dict[act]["codigo"]=n
                else:
                    print("El parametro de la codigo no es correcto")
                    print('''
                            El codigo debe tener, una mayusculas, una minusculas, 
                            un numero y un largo exacto de 6''')
            case 4:
                break
            case _:
                print("Opcion invalida")
def borrar_perros(dict):
    mostrar_perros(dict)
    borrar=int(input("Seleccione el perro a borrar: "))
    del perros[borrar]

while True:
    try:
        print('''
            1.- Resgistra un perro
            2.- Mostrar perros
            3.- Actualizar perro
            4.- Borrar perro
            5.- Salir
            ''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                ingres_perro(perros)
            case 2:
                mostrar_perros(perros)
            case 3:
                act_perros(perros)
            case 4:
                borrar_perros(perros)
            case 5:
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("El error es:", e)