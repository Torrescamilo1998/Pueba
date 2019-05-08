#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Camilo
#
# Created:     07/05/2019
# Copyright:   (c) Camilo 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

def cargarTexto():
    return[x.split() for x in opne ("matriz.txt").readlines ()]
def ImprimirPrimeraPosicion(matriz):
    print matriz [0]

def mostrar(matriz):
    ImprimirPrimeraPosicion(matriz)

    if len(matriz[1:,:]) is not 0:
        mostrar (np.rot90(matriz[1:,:]))


if __name__ == '__main__':
    print ("Matriz original:")
    print np.array(cargarTexto())
    print(" ")

    print("Matriz recorridaen forma de caracol: ")
    mostrar(np.array(cargarTexto()))
