import os
def fnt_limpiar():
    os.system('cls')
def fnt_mensaje(msn):
    fnt_limpiar()
    print('El mensaje es: ', msn)
    
fnt_mensaje('El burrito sabanero')