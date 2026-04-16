#Librerias:

import math
#Funciones:

def area_circulo(r):
    A=math.pi*r**2
    return A

def energia_cinetica(m,v):
    Ec=1/2*m*(v**2)
    return Ec

def energia_potencial(m,h,g):
    Ep=m*g*h
    return Ep


#Cuerpo del programa:

#r=float(input("ingresar el radio de la circunferencia: "))
m=float(input("ingresar la masa del objeto en kg.: "))
v=float(input("ingresar la velocidad del objeto en m/s: "))
h=float(input("ingresar la altura en la que está el objeto en m: "))
g=float(input("ingresar la gravedad en m/s^2: "))
#A=area_circulo(r)
#print("El area del circulo es: ",A)
Ec=energia_cinetica(m,v)
print("La energia cinetica del objeto es: ", Ec, "kg*m/s^2")
Ep=energia_potencial(m,h,g)
print("La energia potencial del objeto es: ", Ep, "kg*m/s^2") 