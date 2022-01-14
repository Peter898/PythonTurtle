'''
Peter Mei

Write a program that stimulates a turtle race.

'''
import time
import turtle
from random import *

#Set the window size
window = turtle.Screen()
window.setup(.75,.75)
window.bgcolor("#f3e3cf")
turtle.hideturtle()
turtle.write("Welcome to the Turtle Racing stimulator \nBy Peter Mei. \nNo turtle were harmed during the creation of the program", font=("Arial",25), align="center")

#creates the turtle
startTurtle = turtle.Turtle()
endTurtle = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

#hide the turtles until game start
startTurtle.penup()
endTurtle.penup()
turtle1.penup()
turtle2.penup()
turtle3.penup()
startTurtle.hideturtle()
endTurtle.hideturtle()
turtle1.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()

#change the shape of the turtles
turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")

finishLine = 600

def game():
    #Set the racing board
    startTurtle.setposition(-600,300)
    endTurtle.setposition(600,300)
    startTurtle.showturtle()
    endTurtle.showturtle()
    startTurtle.right(90)
    startTurtle.write("Start Line", font=("Arial",20),align="center")
    endTurtle.right(90)
    endTurtle.write("Finish Line", font=("Arial",20),align="center")

    #change the thickness of the lines
    startTurtle.pensize(3)
    endTurtle.pensize(3)
    #Chnage the color of the lines
    startTurtle.color("yellow")
    endTurtle.color("green")

    #draw the starting lines and finish lines
    startTurtle.pendown()
    endTurtle.pendown()
    startTurtle.forward(600)
    endTurtle.forward(600)
    startTurtle.hideturtle()
    endTurtle.hideturtle()

    #set and show the turtle at the starting point
    turtle1.setposition(-600,250)
    turtle1.pensize(5)
    turtle2.setposition(-600,0)
    turtle2.pensize(5)
    turtle3.setposition(-600,-250)
    turtle3.pensize(5)
    #change the colors of the turtle
    turtle1.color("black")
    turtle2.color("#33663A")
    turtle3.color("green")

    turtle1.showturtle()
    turtle2.showturtle()
    turtle3.showturtle()

    time.sleep(2)
    #let the game start
    turtle.write("Start", font=("Arial",30),align="center")
    time.sleep(2)

    #Set a random speed for all turtles
    speed1 = randint(0,11)
    turtle1.speed(speed1)
    speed2 = randint(0, 11)
    turtle2.speed(speed2)
    speed3 = randint(0,11)
    turtle3.speed(speed3)
    #using the for loop, have the turtle move forward simultaneously
    for count in range(1,475):
        turtle.clear()
        turtle1.pendown()
        turtle2.pendown()
        turtle3.pendown()
        turtle1.forward(randint(0,20))
        turtle2.forward(randint(0,20))
        turtle3.forward(randint(0,20))

        #Check which turtle wins
        if turtle1.xcor() >= finishLine :
            time.sleep(2)
            window.reset()
            turtle1.color("black")
            turtle1.write("The black turtle won. \nCongratulations!!!!!!!!", font=("Arial",50),align="center")
            break
        elif turtle2.xcor() >= finishLine:
            time.sleep(2)
            window.reset()
            window.bgcolor("#f3e3cf")
            turtle2.color("#33663A")
            turtle2.write("The dark green turtle won. \nCongratulations!!!!!!!!", font=("Arial",50),align="center")
            break
        elif turtle3.xcor() >= finishLine :
            time.sleep(2)
            window.reset()
            window.bgcolor("#f3e3cf")
            turtle3.color("green")
            turtle3.write("The light green turtle won. \nCongratulations!!!!!!!!", font=("Arial",50),align="center")
            break
        else:
            continue


time.sleep(5)
turtle.clear()
game()
turtle.done()