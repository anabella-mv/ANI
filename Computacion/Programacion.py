#Cito librerias necesarias

#import matplotlib.pyplot as plt
#import numpy as np
import math
import random

"""" Funiciones
    def nombre_funcion(parametro1, parametro2):
    # código de la función
    resultado = parametro1 + parametro2
    return resultado

    Variables locales: las que se definen dentro de la función, variables globales, son las de fuera
    
    1. Crear los datos
x = np.linspace(-10, 10, 100)  # 100 puntos entre -10 y 10
y = x**2  # función cuadrática

    2. Graficar
plt.plot(x, y)

    3. Personalizar
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Mi primer gráfico")
plt.grid(True)

    4. Mostrar
plt.show()

Inicializar vectores:
tiempo = np.zeros(N)
Valores iniciales
tiempo[0] = theta0    
aumentar: tiempo[i+1]= algo

Hacer entrenando
"""
def orden_biblio(biblio):
    for i in range(len(biblio)):
        for j in range(len(biblio)):
            if biblio[i][1] < biblio[j][1]:
                aux = biblio[i]
                biblio[i] = biblio[j]
                biblio[j] = aux
    return biblio

def orden_numerico(cjto):
    for i in range(len(cjto)):
        for j in range(len(cjto)):
            if cjto[i] < cjto[j]:
                aux = cjto[i]
                cjto[i] = cjto[j]
                cjto[j] = aux
    return cjto
def adivinanza():
    numero=random.randint(0,100)
    intentos=0
    numero_intento=int(input("Adivina el número entre 0 y 100: "))
    while numero_intento!=numero:
        intentos+=1
        if numero_intento<numero:
            print("Más grande!")
        else:
            print("Más chico")
        numero_intento=int(input("Intenta nuevamente: "))
    print("Correcto! Te tomó ", intentos, " intentos." )

def impares_hasta_n(n):
    impares=[]
    for i in range(1,n,2):
        impares.append(i)
    return impares

def main():
    biblio=[["El Aleph","Borges"],["Rayuela", "Cortazar"],["El tunel", "Sabato"],["Martín Fierro", "Hernandez"]]
    cjto=[2,5,2.9,7,8,6]
    punto=1
    while punto!=0:
        print("Elija el ejercicio a desarrollar:")
        print("Los puntos a ejecutar son 1, 2 , 3 y 4, el 0 es para terminar el programa")
        punto=int(input("Seleccione el punto a desarrollar: "))
        if punto==1:
            print("Ejercicio 1: Ordenar una lista de libros por autor")
            print(orden_biblio(biblio))
        elif punto==2:
            print("Ejercicio 2: Ordenar un conjunto de números")
            print(orden_numerico(cjto))
        elif punto==3:
            print("Ejercicio 3: Juego de Adivinanza: ")
            adivinanza()
        elif punto==4:
            print("Ejercicio 4: Numeros impares hasta n:")
            n=int(input("Ingrese el número hasta el cuando armar la lista de impares: "))
            print("Aviso: si el número es par se mostrará hasta el anterior a él")
            print(impares_hasta_n(n))
        elif punto==0:
            print("Programa terminado")
            break
        else:
            print("Punto no válido, intente nuevamente")
main()  
