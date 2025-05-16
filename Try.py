import random

def suma():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese otro numero "))
    print("El resultado de la suma es", n1+n2)
def resta():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese un numero "))
    print("El resultado de la resta es", n1-n2)
def multiplicacion():
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese un numero "))
    print("El resultado de la multiplicacion es", n1*n2)
def dividir():
    try:
        n1=int(input("Ingrese un numero "))
        n2=int(input("Ingrese un numero "))
        print("El resultado de la division es", n1/n2)
    except ZeroDivisionError as nombre_de_excepcion:
        print(f"Se produjo una excepción: {nombre_de_excepcion}")
# suma()
# resta()
# multiplicacion()
# dividir()

def calculadora():
    while True:
        try:
            op=int(input('''Ingrese una opcion
                        1.- Suma
                        2.- Resta
                        3.- Multiplicacion
                        4.- Dividir   
                        5.- Saliendo              
                        '''))
            match op:
                case 1:
                    print("suma")
                    suma()
                case 2:
                    print("resta")
                    resta()
                case 3:
                    print("multiplicacion")
                    multiplicacion()
                case 4:
                    print("dividir")
                    dividir()
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("Opcion INVALIDA")
        except Exception as error:
            print("Solo puede ingresar numeros, no caracteres")
            print("ERROR", error)


calculadora()

def azarN():
    num=random.randint(1,5)
    return num
print(azarN()*10)


# try:
#     op=int(input("Ingrese un numero"))
# except Exception:
#     print("Solo puede ingresar numeros, no caracteres")

# Try:
# # Código que podría generar una excepción
# # Dentro de este bloque de código, debes colocar
# # lo que quieres validar por medio de una
# # excepción, ejemplo, operaciones matemáticas,
# # Set de variables, etc....
# resultado = 10/ 0
# except ZeroDivisionError as nombre_de_excepcion:
# # Código para manejar la excepción
# print(f"Se produjo una excepción: {nombre_de_excepcion}")
# else:
# # Código a ejecutar si no se produjo ninguna excepción
# print("No se produjo ninguna excepción")
# finally:
# # Código a ejecutar siempre, independientemente de si se produjo
# una excepción o no
# print("Este bloque se ejecuta siempre")

