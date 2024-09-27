import os
import math

def est_des_con_limites():
    limite_inf = []
    limite_sup = []

    datos = int(input("ingrese el tamaño de su cuadro en filas: "))
    poblacional_muestral = str(input("La consigna es poblacional o muestral? (p/m):"))

    print("Ingrese todos los valores de intervalos primeros los inferiores luego los superiores")
    for i in range(datos):
        limite_inf.append(float(input("")))   
        limite_sup.append(float(input("")))
    
    #Marca de clase ci:
    ci = []

    print("Ingresa las marca de clase")
    for i in range(datos):
        ci.append(float(input("")))
    
    #fi
    fi = []

    print("Ingresa los fi")
    for i in range(datos):
        fi.append(float(input("")))
    
    #fi
    Fi = []

    print("Ingresa los Fi")
    for i in range(datos):
        Fi.append(float(input("")))

    #La moda
    mas_repetido = fi.index(max(fi))

    print("La moda es: ", ci[mas_repetido])

    #La mediana
    mediana = Fi[-1]/2
    
    print("La mediana es: fíjate cual esta mas cerca de", round(mediana, 1))
    
    #Promedio o media aritmética:
    promedio = 0
    for i in range(datos):
        promedio += ci[i]*fi[i]
    
    promedio /= Fi[-1]

    print("El promedio o media aritmética es: ", round(promedio,2))

    varianza = 0 
    #Varianza
    for i in range(datos):
        varianza += ((ci[i]-promedio)**2)*fi[i]
    if poblacional_muestral == "p":
        varianza /= Fi[-1]
    else:
        varianza /= Fi[-1]-1

    print("La varianza es:",round(varianza,2))

    #Desvió
    desvio = round((math.sqrt(varianza)),2)

    print("El desvió es: ", desvio)
    
    #Coeficiente de variación
    cv = round(((desvio/promedio)*100),2)

    print("La coeficiente de varianza es:",cv)

    maximo_soli = int(input("Cual es el numero que buscas los menores a ese: "))

    maximo = limite_sup.index(maximo_soli)
    porcentaje=0
    for i in range(maximo+1):
        porcentaje += fi[i]
    porcentaje = (porcentaje/Fi[-1])*100

    print("El",round(porcentaje,2),"'%' de los datos es menor a",maximo_soli)

    porcentaje_solicitado = float(input("ingrese el porcentaje que quiera buscar"))

    aprox = (porcentaje_solicitado/100)*Fi[-1]

    aprox = Fi.index(aprox)

    print("De las precipitaciones medidas, el aproximadamente el ", porcentaje_solicitado , "'%' son inferiores a ",limite_sup[aprox] )

    os.system("pause")