import random
import time
while True:
    try:
        perros=int(input("Ingrese la cantidad de perros: "))
        while perros<1:
            print("Debe ingresar uno o mas perros")
            perros=int(input("Ingrese la cantidad de perros: "))
        cuota=4
        cumplen=0
        print("Los perros salieron a cazar!!!")
        for p in range(perros):
            conejos=random.randint(0,8)
            time.sleep(1)
            if cuota<=conejos:
                print(f"El perro {p+1} trajo {conejos} conejos, cumplio la cuota")
                cumplen+=1
            else:
                print(f"El perro {p+1} trajo {conejos} conejos, se queda sin filete")
        print(f"El total de perros que cumplio la cuota fue {cumplen}")
        print(f"El total de perros que no cumplio la cuota fue {perros-cumplen}")
        break
    except Exception:
        print("Solo ingrese numeros enteros")

##                       _.-**-._
#                     _,(        ),_
#                  .-"   '-^----'   "-.
#               .-'                    '-.
#             .'                          '.
#           .'    __.--**'""""""'**--.__    '.
#          /_.-*"'__.--**'""""""'**--.__'"*-._\
#         /_..-*"'   .-*"*-.  .-*"*-.   '"*-.._\
#        :          /       ;:       \          ;
#        :         :     *  !!  *     :         ;
#         \        '.     .'  '.     .'        /
#          \         '-.-'      '-.-'         /
#       .-*''.                              .'-.
#    .-'      '.                          .'    '.
#   :           '-.        _.._        .-'        '._
#  ;"*-._          '-._  --___ `   _.-'        _.*'  '*.
# :      '.            `"*-.__.-*"`           (        :
#  ;      ;                 *|                 '-.     ;
#   '---*'                   |                    ""--'
#    :                      *|                      :
#    '.                      |                     .'
#      '.._                 *|        ____----.._-'
#       \  """----_____------'-----"""         /
#        \  __..-------.._        ___..---._  /
#        :'"              '-..--''          "';
#         '""""""""""""""""' '"""""""""""""""'
