import os
def fnt_calcularV(distancia, tiempo):
    global velocidad
    velocidad = distancia / tiempo
    
def fnt_mensaje(msn):
    print(msn, ' ', velocidad, 'Km/h')

fnt_calcularV(450,3)
fnt_mensaje('La velocidad promedio es:')
