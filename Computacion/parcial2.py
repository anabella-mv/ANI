#Cito librerias necesarias

import matplotlib.pyplot as plt
import numpy as np
import math

#Funcion trascendental: f(x)=xcos(x)-ln(x+2)
def f(x):
    return x*math.cos(x)-math.log(x+2)
#Metodo de bisección
def rbisec(fun,I,err,mit):
    a,b=I[0],I[1]
    fa, fb=fun(a), fun(b)
    if fa*fb>0:
        print("NO es posible aplicar el método")
        return None
    

    #Iteraciones
    for i in range (mit):
        e=(b-a)/2
        c=a+e
        fc=fun(c)

        if abs(fc)<err:
            print("La raiz es ", c, " con un error de +- ",e, " o por lo menos satisface el error aceptado, con valor ", fc)
            break
        if fa*fc<0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
    #Contar iteraciones
    num_iter=i+1
    print("se alcanzó el error aceptado en ", num_iter, " iteraciones")
    return None

#Funcion principal
def main():
    punto=-1
    print("Inicio del programa del parcial 2 de computación")
    while punto!=0:
        
        punto=int(input("Ingrese el número del punto a ejecutar 1 y 2 o 0 para salir: "))
        if punto==1:
         #Crear los datos
            x = np.linspace(-1.5, 10, 100)  
            y = [f(i) for i in x]  # función trascendental

            #Graficar
            plt.plot(x, y)

            #Personalizar
            plt.xlabel("Eje X")
            plt.ylabel("Eje Y")
            plt.title("Gráfico de la función trascendental")
            plt.grid(True)

            #Mostrar
            plt.show()
        elif punto==2:
            print("Para identificar tres intervalos distintos donde las funciones tengan raíces,se puede utilizar el método de bisección, como es una función continua se puede evaluar en diferentes puntos para encontrar cambios de signo, lo que indicaría la presencia de una raíz. Por ejemplo, se pueden evaluar los siguientes intervalos:")
            print("1. [-1.5, -0.5]")
            print("2. [0.5, 2.5]")
            print("3. [7.5, 9.5]")
            error=10**(-6)
            mit=100
            print("Intervalo 1: [-1.5, -0.5]")
            I=[-1.5, -0.5]
            rbisec(f,I,error,mit)
            print("Intervalo 2: [5, 6]")
            I=[5, 6]
            rbisec(f,I,error,mit)
            print("Intervalo 3: [7.5, 8]")
            I=[7.5, 8]
            rbisec(f,I,error,mit)           
        elif punto==0:
            print("Se termina el punto actual.")
            break
        else:
            print("Número de punto no válido. Por favor, ingrese un número entre 1 y 3, o 0 para salir.")
main()