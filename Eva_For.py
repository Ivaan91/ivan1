total=0
cant=0
desc=0
pikachu=0
otaku=0
pulpo=0
anguila=0
print("Bienvenido, a Shushitumare")

while True:
    op=int(input('''
        ¿Que desea ordenar?
        1. Pikachu Roll $4500
        2. Otaku Roll $5000
        3. Pulpo Venenoso Roll $5200
        4. Anguila Eléctrica Roll $4800
        5. Finalizar Orden
        :'''))
    match op:
        case 1:
            cant+=1
            total=total+4500
            pikachu=pikachu+1
        case 2:
            cant+=1
            total=total+5000
            otaku=otaku+1
        case 3:
            cant+=1
            total=total+5200
            pulpo=pulpo+1
        case 4:
            cant+=1
            total=total+4800
            anguila=anguila+1
        case 5:
            print("Orden completada")
            print('''¿Posee codigo de descuento?
                  1.- Si
                  2.- No
                  ''')
            desc=int(input())
            if desc==1:
                while True:
                    cod=input("Ingrese su codigo de descuento")
                    

            break
        case _:
            print("Opcion Invalida")
