import random
import time
j1=0
j2=0
dado=0
meta=30
turno=1
while j1<=j2 and j1>=j2:
    if turno % 2==0:
        print("Turno de J1")
        time.sleep (1)
        dado=random(1,6)
        j1=+dado
        print("El J1 saco ", dado)
        print("Avanza hasta la casilla ", j1)
    else:
        print("Turno de J2")
        time.sleep (1)
        dado=random(1,6)
        j2=+dado
        print("El J2 saco ", dado)
        print("Avanza hasta la casilla ", j2)