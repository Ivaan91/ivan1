total=0
cant=0
nombre=input("Ingrese su nombre: ")


while True:
    op=int(input('''
        Que productos llevara?
        1.- Coca-cola 3L $2500
        2.- Doritos $1000
        3.- Pan de molde XL $3000
        4.- Pizza congelada $4000
        5.- Salir
        : '''))
    match op:
        case 1:
            cant+=1
            total=total+2500
        case 2:
            cant+=1
            total=total+1000
        case 3:
            cant+=1
            total=total+3000
        case 4:
            cant+=1
            total=total+4000
        case 5:
            break
        case _:
            print("Opcion Invalida")


print(f'''
############################################     
# Su boleta es de:                         
# EL total de productos que lleva: {cant}  
# El total neto es: {total}                
# El total del IVA es: {total*1.19}         
#                                          
# Gracias por su compra {nombre}                     
############################################
  ''')
#                        _.-**-._
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