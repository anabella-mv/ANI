#Cito librerias necesarias:
import math
import random
import matplotlib.pyplot as plt
import numpy as np

#Primera función: Tirar dos dados y sumarlos
def tirar_dados():
    #Tirada de dados
    dado1 = random.randint(1, 6)
    #print("Primer valor del dado: ", dado1)
    dado2 = random.randint(1, 6)
    #print("Segundo valor del dado: ", dado2)

    #Resultado
    total = dado1 + dado2
    #print("Suma de los dados: ", total)
    return total

#Segunda función: tirar los dados en un bucle solicitado
def tirada_bucle(n):
    #Creo la lista de tiradas
    tiradas=[]
    #En bucle solicitado
    for i in range(n):
        #tira los dados
        tirada=tirar_dados()
        #guarda el resultado en una lista
        tiradas.append(tirada)
    return tiradas

#Tercera función: historigrama de 10000 tiradas
def histograma_tiradas(tiradas):
    N=10000
    #Creo la lista de tiradas
    N_tiradas=tiradas(N)
    #Creo el histograma
    tiradas_total, bordes_bins=np.histogram(N_tiradas, bins=11)
    #Grafico el histograma
    plt.hist(N_tiradas, bins=11)
    plt.title("Historigrama de 10 mil tiradas")
    plt.xlabel("Suma de los dados")
    plt.ylabel("Frecuencia")

    plt.show()
    return None

#Funcion para jugar
def jugar():
    print("Bienvenido al juego del 21")
    total=0
    contador=0
    #Trabaja con un bucle hasta que el valor esperado sea igual a 21
    while total!=21:
        #Tirada
        contador=contador+1
        total=tirar_dados() + total
        if total<21:
            #Cuando es menor simplemente muestra el resultado y sigue tirando
            resultado=21-total
            #print("Te falta ", resultado, " para llegar a 21")
        else:
            #Cuando es mayor muestra el resultaddo y resta el excedente
            resultado=total-21
            #print("Te sobra ", resultado, " para llegar a 21")
            #print("Te pasaste del 21, ahora se resta el valor sobrante para continuar jugando...")
            total=21-resultado
    print("¡GANASTEEEEEE!")
    return contador
def jugar_bucle(p):
    #Crea lista de tiradas:
    cant_tiradas=[]
    for i in range(p):
                #Se guarda los intentos para ganar en cada partida por el contador que devuelve
                cant_tiradas.append(jugar())
    return cant_tiradas
def histograma_partidas(jugar):
    M=1000
    #Creo la lista de tiradas necesarias para ganar cada partida de 21
    M_juegos=jugar_bucle(M)
    #Creo el histograma
    juegos_total, bordes_bins=np.histogram(M_juegos, bins=11)
    #Grafico el histograma
    plt.hist(M_juegos, bins=11)
    plt.title("Historigrama de mil juegos")
    plt.xlabel("Cantidad de tiradas para ganar")
    plt.ylabel("Frecuencia")

    plt.show()
    return None
def main():
    punto=-1
    print("Inicio del programa del parcial 2 de computación")
    while punto!=0:
        
        punto=int(input("Ingrese el número del punto a ejecutar (1-6) o 0 para salir: "))
        if punto==1:
            print("Ejercicio 1: Tirar dos dados y sumarlos")
            tirar_dados()
        elif punto==2:
            print("Ejercicio 2: Tirar los dados en un bucle solicitado")
            n=int(input("Ingrese el número de tiradas que desea realizar: "))
            print(tirada_bucle(n))
        elif punto==3:
            print("Ejercicio 3: Histograma de 10000 tiradas")
            histograma_tiradas(tirada_bucle)
        elif punto==4:
            print("Ejercicio 4: Juego del 21")
            jugar()
        elif punto==5:
            print("Ejercicio 7: Jugar al 21 en bucle")
            p=int(input("INgrese la cantidad de partidas que quiera jugar, al final se mostrará la cantidad de tiradas necesarias para ganar cada partida:"))
            #Llamo a la función para jugar la cantidad de veces que yo quiera
            cant_tiradas=jugar_bucle(p)
            print("Cantidad de tiradas necesarias para ganar cada partida: ", cant_tiradas)
        elif punto==6:
            print("Ejercicio 8: Histograma de partidas e intentos para ganar cada partida")
            histograma_partidas(jugar)
        elif punto==0:
            print("Fin del programa, gracias por participar")
main()