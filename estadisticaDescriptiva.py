import os

def estadisticaDescriptiva():
    #solicitamos entrada de datos
    datos = int(input("Con cuantos datos está trabajando? "))
    #solicitamos ingreso de lista de numeros (su tamaño depende de la cantidad de datos)
    lista = []
    print("Ingrese los datos: ")
    for i in range(datos):
        guardado = int(input(""))
        lista.append(guardado)
    os.system("cls")
    #chequeamos cuantas veces se repite cada numero
    fi = []
    xi = []
    for i in range(datos):
        guardaConteo = lista.count(i)
        if guardaConteo != 0:
            fi.append(guardaConteo)
            xi.append(i)
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
    print("Moda:", moda)
    #mediana. si es Par, entonces n/2. si es Impar, entonces (n-1)/2
    if tamfi%2 == 0:
        mediana = tamfi / 2
    else:
        mediana = (tamfi-1) / 2 
    print("Mediana:" , int(mediana))
    #media aritmética o promedio
    suma = 0
    for i in range(tamfi):
        suma += fi[i] * xi[i]
    promedio = suma / datos
    print("Media aritmetica/promedio:", round(promedio,2))
    #varianza poblacional o muestral 


    #desvío estandar o muestral

    #coeficiente de variación

    os.system("pause")

