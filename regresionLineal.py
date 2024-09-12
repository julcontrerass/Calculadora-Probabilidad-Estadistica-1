import math
import os

def regresionLineal():
    os.system("cls")
    # necesitamos conocer los valores de X (independiente) e Y (dependiente)
    arrayX = []
    arrayY = []
    tamanio = int(input("ingrese cantidad de datos de la tabla: "))
    print("Ingrese todos los valores de x:")
    for i in range(tamanio):
        ingresoX = int(input(""))
        arrayX.append(ingresoX) #push hace que el ingreso anterior, se ponga en el array
    print("Ingrese todos los valores de y:")
    for i in range(tamanio):
        ingresoY = int(input(""))
        arrayY.append(ingresoY)


    #ahora tenemos que calcular el promedio de X y de Y
    promedioX = sum(arrayX) / tamanio
    promedioY = sum(arrayY) / tamanio

    #ahora necesitamos varianza de X y de Y
    sumaVarianzaX = 0
    sumaVarianzaY = 0
    for i in range(tamanio):
        sumaVarianzaX += (arrayX[i] - promedioX) **2
        sumaVarianzaY += (arrayY[i] - promedioY) **2

    muestra = int(input("EL ENUNCIADO ES MUESTRAL (0) O POBLACIONAL (1)?"))
    if muestra == 0:
        varianzaX = sumaVarianzaX / tamanio
        varianzaY = sumaVarianzaY / tamanio
    else:
        varianzaX = sumaVarianzaX / (tamanio - 1)
        varianzaY = sumaVarianzaY / (tamanio - 1)

    #ahora necesitamos covarianza cov(XY)
    covarianza = 0
    for i in range(tamanio):
        covarianza += arrayX[i]*arrayY[i]
    covarianza = (covarianza / tamanio) - promedioX * promedioY

    #ahora necesitamos desvío de X y de Y
    desvioX = math.sqrt(varianzaX)
    desvioY = math.sqrt(varianzaY)

    #ahora necesitamos la pendiente (b)
    pendiente = covarianza / varianzaX

    #ahora necesitamos la ordenada (a)
    ordenada = promedioY - pendiente * promedioX

    #ahora necesitamos la r (coeficiente de correlación, regresión o de Pearson)
    coeficientePearson = covarianza / (desvioX * desvioY)

    #ahora necesitamos la r al cuadrado (coeficiente de determinación)
    coeficienteDeterminacion = coeficientePearson **2

    os.system("cls")
    print(arrayX)
    print(arrayY)
    print("resultados:")
    print("promedio de X:" , promedioX)
    print("promedio de Y:", promedioY)
    print("varianza de X:", varianzaX)
    print("varianza de Y", varianzaY)
    print("covarianza:", covarianza)
    print("desvío de X:", desvioX)
    print("desvío de Y:", desvioY)
    print("pendiente:", pendiente)
    print("ordenada:", ordenada)
    print("coeficiente de Pearson o r:", coeficientePearson)
    print("coeficiente de determinación o r**2:", coeficienteDeterminacion)

    os.system("pause")

    







