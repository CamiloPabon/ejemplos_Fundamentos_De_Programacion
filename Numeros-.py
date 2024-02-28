"""Leer sucesivamente números del teclado y
Visualizar la suma de los números impares
Obtener el promedio de los números pares
Contar los números negativos
Obtener el promedio de los números mayores de 50.
"""
# Inicializar variables

SumaImpares = 0
SumaPares = 0
CantidadPares = 0
CantidadNegativos = 0
SumaMayores50 = 0
cantidadMayores50 = 0
Numero = int
desicion=""

# Ciclo para leer los números
while True:
    desicion=input("Desea ingresar un número? S/N: ")
    if desicion=="N" or desicion=="n":
        break
    print("Ingrese los números, para terminar ingrese N")
    Numero = int (input("Ingrese el número: "))
    if Numero < 0:
        CantidadNegativos += 1
    elif Numero % 2 == 0:
        SumaPares += Numero
        CantidadPares += 1
    elif Numero % 2 != 0:
        SumaImpares += Numero
    elif Numero > 50:
        SumaMayores50 += Numero
        cantidadMayores50 += 1
    else:
        print("Ingrese un Formato válido")
# Calcular promedios
print("La suma de los números impares es: ", SumaImpares)
print("La cantidad de números negativos es: ", CantidadNegativos)
if CantidadPares == 0:
    print("No hay números pares")
else:
    PromedioPares = SumaPares / CantidadPares
    print("El promedio de los números pares es: ", PromedioPares)
if cantidadMayores50 == 0:
    print("No hay números mayores a 50")
else:
    PromedioMayores50 = SumaMayores50 / cantidadMayores50s
    print("El promedio de los números mayores a 50 es: ", PromedioMayores50)
    
    





