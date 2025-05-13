# uso y explicacion de match

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
    n1=int(input("Ingrese un numero "))
    n2=int(input("Ingrese un numero "))
    print("El resultado de la division es", n1/n2)

# suma()
# resta()
# multiplicacion()
# dividir()

def calculadora():
    while True:
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

calculadora()
