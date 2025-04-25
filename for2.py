total=0

cant=int(input("cuantos productos llevara"))
for i in range (cant):
    print('''
    Que producto llevara?
    1.- Diazepam $9000
    2.- Metametazona $10500
    3.- Oblea china $1000 ''')
    op=int(input())
    if op==1:
        print("Usted lleva Diaezepam")
        total=total+9000
    elif op==2:
        print("Usted lleva Metametazona")
        total=total+10500
    elif op==3:
        print("Usted lleva Oblea china")
        total=total+1000
    else:
        print("Opcion no valida")
print("El total neto es ", total)
print("El total del IVA es ", total*1.19)