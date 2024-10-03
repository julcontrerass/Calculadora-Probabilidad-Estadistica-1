import os
import math

def estadistica_escriptiva():
    #vemos si la cosigna nos da el fi o no
    fiSiNo = input("La consigna tiene fi? (s/n) ").lower()

    if fiSiNo == "n":
        datos = int(input("Con cuantos datos está trabajando? "))
        #solicitamos ingreso de lista de numeros (su tamaño depende de la cantidad de datos)
        lista = []
        print("Ingrese los datos: ")
        for i in range(datos):
            guardado = int(input(""))
            lista.append(guardado)
        #chequeamos cuantas veces se repite cada numero
        fi = []
        xi = []
        for i in range(datos):
            guarda_conteo = lista.count(i)
            if guarda_conteo != 0:
                fi.append(guarda_conteo)
                xi.append(i)
    elif fiSiNo == "s":
        # Pedimos la cantidad de filas para ver que tamaño tenemos que usar
        datos = int(input("Cual es la cantidad de filas que posee su tabla? "))
        xi = []
        fi = []
        print("Ingrese los valores de xi:")
        for i in range(datos):
            xi.append(int(input("")))
        print("Ingrese los valores de fi:")
        for i in range(datos):
            fi.append(int(input("")))
    poblacional_muestral = str(input("La consigna es poblacional o muestral? (p/m):"))
    os.system("cls")
    #con esos datos obtendremos los valores de xi y de fi
    print("Tabla xi:", xi)
    print("Tabla fi:", fi)


    #Fi, su primer valor es igual que el primer fi. (el resultado final de FI debe ser igual a la cantidad total de datos). (este es el que se acumula)
    tamfi = len(fi)
    Fi = []
    for i in range(tamfi):
        if i == 0:
            Fi.append(fi[i])
        else:
            Fi.append(fi[i] + Fi[i-1])
    print("Tabla Fi:", Fi)
    #hi o fr. esto es la division entre el fi dividido el total de datos
    hi = []
    for i in range(tamfi):
        division =fi[i] / datos
        hi.append(round(division,2))
    print("Tabla hi:" , hi)
    #Hi o Fr. el primer valor de Hi es igual al primer valor de hi. se acumulan los valores de hi.
    Hi = []
    for i in range(tamfi):
        if i == 0:
            Hi.append(hi[i])
        else:
            suma = hi[i]+Hi[i-1]
            Hi.append(round(suma,2))
    print("Tabla Hi:",Hi)
    #moda
    moda = fi.index(max(fi))
    if xi[0] == 0:
        print("Moda:", moda)
    else:
        print("Moda:", moda+1)
    #mediana. si es Par, entonces n/2. si es Impar, entonces (n-1)/2
    if tamfi % 2 == 0:
        mediana = tamfi / 2
    else:
        mediana = (tamfi-1) / 2 
    print("Mediana:" , int(mediana))
    #media aritmética o promedio
    suma = 0
    for i in range(tamfi):
        suma += fi[i] * xi[i]
    promedio = suma / datos
    print("Media aritmética/promedio:", round(promedio,2))
    #varianza poblacional o muestral. se hace la ((xi-promedio)^2 * fi)/datos (si es muestral es datos-1)
    varianza = 0
    
    if poblacional_muestral == "p":
        for i in range(tamfi):
            varianza += ((xi[i]-promedio)**2) * fi[i]
        varianza /= datos
        

    else:
        for i in range(tamfi):
            varianza += ((xi[i]-promedio)**2) * fi[i]
        varianza /= (datos-1)
    
    print("La varianza es:",round(varianza,3))
 
    #desvío estandar o muestral es la raiz de la varianza
    desvio = math.sqrt(varianza)

    print("La el desvió es:",round(desvio,3))

    #coeficiente de variación
    coeficiente_variacion = (desvio/promedio) * 100
    print("La coeficiente de variación es:%",round(coeficiente_variacion,3))

    os.system("pause")

