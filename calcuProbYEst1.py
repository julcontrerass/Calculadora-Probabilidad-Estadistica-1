from regresionLineal import regresion_lineal
from estadisticaDescriptiva import estadistica_escriptiva
from estadisticaDescConLimites import est_des_con_limites
import os

while True:
    os.system("cls")
    print("--- Menú Principal ---")
    print("1. Calculadora estadistica descriptiva")
    print("2. Calculadora regresión lineal")
    print("3. Calculadora estadistica descriptiva con limites")
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
            regresion_lineal()
        case 3:
            os.system("cls")
            print("Calculadora de estadistica descriptiva con limites\n")
            est_des_con_limites()
        case 0:
            print("Saliendo del programa...")
            break  
        case _: 
            print("Valor ingresado invalido")

