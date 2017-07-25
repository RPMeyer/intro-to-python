#*******************************
# ws ch7_4
#
# Write a function a function, stop_when_circle_xd(t,Dz,R),
# which makes the turtle t execute a random walk of size Dz
# for each step, and which stops the first time the turtle
# is >= radius of R from its start point.
# Use a separate turtle to draw a circle of radius R
# Uses the turtle position()
# Function, which returns the x and y coordinate for the current
# Position of the turtle.
# Print out the number of steps the turtle takes before
# stopping.
#*******************************
import turtle
import random
testTurt = turtle.Turtle()
testTurt.speed(0)


def turtleInit(bgColor, wnInfo, speed):
    '''initializes turtle'''
    wn = turtle.Screen()
    wn.bgcolor(bgColor)
    wn.title(wnInfo)

def find_hypot(s1,s2):
    '''given the length of two sides of a right triangle, returns the length of the hypotenuse'''
    hypotenuse = ((s1**2)+(s2**2))**(1/2)

    return hypotenuse

def drawCircle(t, R):
    '''draw circle of (radius) radius with turtle (t) CENTERED IN WINDOW'''
    t.penup()
    t.goto(0,-R)
    t.pendown()
    t.circle(R)
    t.penup()
    t.home()
    t.pendown()

def stop_when_circle_xd(t,Dz,R):
    '''makes the turtle t execute a random walk of size Dz
    for each step AND which stops the first time the turtle
    is >= radius of R from its start point
    PRINT out the number of steps the turtle takes before
    stopping'''
    drawCircle(t,R)

    while t.distance(0,0) < R:
        t.left(random.randint(0,359))
        t.forward(Dz)
#Use a separate turtle to draw a circle of radius R
#Uses the turtle position()

turtleInit('lightgreen', 'stopping turtle when radius from origin', .5)
#drawCircle(testTurt,150)
stop_when_circle_xd(testTurt, 15, 150)
