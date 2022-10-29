from pickle import TRUE
import turtle as t
import time 
import random


delay_time=0.1


#finestra snake
t.bgcolor("black")                  #genera el espai per on es mou la serp
t.title("Snake")
t.setup(width=600, height=600)
t.tracer(0)
t.mainloop

#snake's head
head=t.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.goto(0,0)
head.direction="stop"                     #direccio cap a on s'hauria de moure la serp al inici
head.penup()
 
#snake's body
cuerpo=[]

#comida
comida=t.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)                     



#funcions
def arriba():                           #definim les diferents direccions de moviment que hi ha
    head.direction="up"
def abajo():
    head.direction="down"
def left():
    head.direction="left"
def right():
    head.direction="right"



def mov():
    if head.direction=="up":
        y=head.ycor()               #guarda coordenada y en la variable
        head.sety(y+20)             #mueve la cabeza 20 pixeles en el eje y

    if head.direction=="down":
        y=head.ycor()               
        head.sety(y-20)             #sety para el eje y
    
    if head.direction=="left":
        x=head.xcor()               #guarda coordenada x en la variable
        head.setx(x-20)             #mueve la cabeza 20 pixeles en el eje x
    
    if head.direction=="right":
        x=head.xcor()               
        head.setx(x+20)             #setx para el eje x

#teclado
t.listen()
t.onkeypress(arriba, "Up")   #U majuscula pq llegeix la fletxa del teclat
t.onkeypress(abajo, "Down")
t.onkeypress(right, "Right")
t.onkeypress(left, "Left")




while True:
    t.update()
    if head.distance(comida)<20:      #marca la distancia de "colision", el 20 son 20 pixeles (manzana y head son de 20x20 pix, asi q si estan a menos de 20 pix es q han colisionado) 
       x=random.randint(-280,280)     #coordenadas de spawn de la fruta en x
       y=random.randint(-280,280)
       comida.goto(x,y)
      
       t.mainloop

       cuerpo=t.Turtle()
       cuerpo.speed(0)
       cuerpo.shape("triangle")
       cuerpo.color("green")
       cuerpo.penup()
       cuerpo.append(cuerpo)
       
    #mover cuerpo serpiente
    totCuer=len(cuerpo)
    
    t.mainloop
    mov()
    time.sleep(delay_time)

    t.mainloop
