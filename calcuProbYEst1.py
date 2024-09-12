# Importar la función regresionLineal desde el archivo regresionLineal.py
from regresionLineal import regresionLineal

while True:
    print("\n--- Menú Principal ---")
    print("1. Ejecutar regresión lineal")
    print("0. Salir")

    opcion = int(input("Ingresa tu opción: "))

    match opcion:
        case 1:
            print("\nEjecutando regresión lineal...\n")
            regresionLineal()
        case 0:
            print("Saliendo del programa...")
            break  
        case _: 
            print("Valor ingresado invalido")

