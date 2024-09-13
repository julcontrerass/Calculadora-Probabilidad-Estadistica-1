from regresionLineal import regresion_ineal
from estadisticaDescriptiva import estadistica_escriptiva

import os

while True:
    os.system("cls")
    print("--- Menú Principal ---")
    print("1. Calculadora estadistica descriptiva")
    print("2. Calculadora regresión lineal")
    print("0. Salir")

    opcion = int(input("Ingresa tu opción: "))

    match opcion:
        case 1:
            os.system("cls")
            print("Calculadora de estadistica descriptiva\n")
            estadistica_escriptiva()
        case 2:
            os.system("cls")
            print("Calculadora regresión lineal\n")
            regresion_ineal()
        case 0:
            print("Saliendo del programa...")
            break  
        case _: 
            print("Valor ingresado invalido")

