#Random & RGB
#Sadie Wood

#init
import turtle
import random #functions that add randomness 
sadie = turtle.Turtle()
sadie.speed(10)
turtle.colormode(255)#Allows us to represent our colors as RGB triplets

#Functions
def dotScreen():
    for index in range(250):
        sadie.penup()
        sadie.goto(random.randint(-500,500),random.randint(-500,500))
        sadie.dot(random.randint(25,300), random.randint(0,255),random.randint(0,255),random.randint(0,255))#A function that we use a lot
        sadie.pendown()

def squares():
    sadie.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    sadie.begin_fill()
    size = random.randint(10,250)
    for index in range(3):
        sadie.forward(size)
        sadie.right(90)
    sadie.end_fill()
        
def squareScreen():
    for index in range(30):
        sadie.penup()
        sadie.goto(random.randint(-500,500),random.randint(-500,500))
        squares()
        sadie.pendown()

def shapeCollage():
    dotScreen()
    squareScreen()
            
#Main
shapeCollage()

