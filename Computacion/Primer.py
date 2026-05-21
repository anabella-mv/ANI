#Librerias:

import math

suma = 0

numero = int(input("Número (0 para terminar): "))

while numero != 0:

    suma = suma + numero   # acumulamos

    numero = int(input("Número (0 para terminar): "))

print("Suma total:", suma)