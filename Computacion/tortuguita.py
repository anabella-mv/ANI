#librerias
import turtle

#Tortuguitaaaa:
torti=turtle.Turtle()
color_linea="green"  #Color de la linea
torti.color(color_linea)
torti.shape("turtle")

#Movimientos de torti:
print("Hola, vamos a hacer que torti haga un rectángulo, para eso necesitamos que ingreses el alto y el ancho del rectángulo: ")
h=int(input("Ingrese el alto del rectángulo: "))  
b=int(input("Ingrese el ancho del rectángulo: ")) 
angulo=90  #Angulo del cuadrado
ang=120

#Hola torti, movete torti como un rectangulo y portate bien:
torti.penup()
torti.goto(-300,-300)
torti.pendown()

v=1
while v<=2:
    torti.forward(b)
    torti.left(angulo)
    torti.forward(h)
    torti.left(angulo)
    v=v+1

#casita
#techo
torti.penup()
torti.goto(-300+b,-300+h)
torti.pendown()
torti.goto(-300+(b/2),-300+(h/3)+h)
torti.goto(-300,-300+h) 

#puerta
torti.penup()
torti.goto((2*b/3)-300,-300)
torti.pendown()

torti.goto((2*b/3)-300,2*h/3-300)
torti.left(180)
torti.forward(b/3)
torti.left(90)
torti.forward(2*h/3)

#pomo
torti.penup()
torti.goto((7*b/12)-300,h/3-300)
torti.pendown()
torti.dot(10)


#frase
torti.penup()
torti.goto(b/3-300,2*h/3+10-300)
torti.pendown()
torti.write("hogar, dulce hogar", font=("Comic Sans MS", 10, "normal"))

turtle.done()