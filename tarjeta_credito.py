deuda=100000
pagoTC=0
monto=0

def pagar_tarjeta(deuda):
    # deuda=100000
    # pagoTC=0
    print(f"Monto de su deuda ${deuda}")
    pagoTC=int(input("Ingrese monto a pagar: $"))
    if pagoTC>=0:
        print(f"El saldo de su deuda es de {deuda-pagoTC}")
    else:
        print("")


def simular_compras(deuda):
    for i in range ()
    print("Menu de compras")
    monto=int(input("Ingrese el monto de su compra: $"))






def menu():
    while True:
        while True:
            op=int(input('''
                Menu de opciones:
                1.- Pagar Tarjeta de credito
                2.- Realizar compra
                3.- Salir
                : '''))
            match op:
                case 1:
                    print("Pagar Tarjeta de credito")
                    pagar_tarjeta()
                case 2:
                    print("Realizar compra")
                    simular_compras()
                case 3:
                    print("Saliendo")
                    break

                    
