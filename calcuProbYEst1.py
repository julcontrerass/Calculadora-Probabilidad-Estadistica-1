from regresionLineal import regresionLineal
from estadisticaDescriptiva import estadisticaDescriptiva

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
            estadisticaDescriptiva()
        case 2:
            os.system("cls")
            print("Calculadora regresión lineal\n")
            regresionLineal()
        case 0:
            print("Saliendo del programa...")
            break  
        case _: 
            print("Valor ingresado invalido")

