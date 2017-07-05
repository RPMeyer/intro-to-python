# ***************************************
# WS ch3_4B:
# Use rectangle(t,w,h) to write a function,
# pinwheel_1(t,w,h,n), that uses rectangle(t,w,h) to
# make a pinwheel using turtle, t. n is an int that tells
# how many rectangles to make within a turn of 360
# degrees.
# ***************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a rectangle using a FUNCTION")
alex = turtle.Turtle() #CREATES THE TURTLE
alex.speed(10)

def rectanglePrint(t,w,h):
    '''Draws a rectangle of width w, height h, using turtle t'''
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

rectanglePrint(alex,150,300)

def pinwheel_1(t,w,h,n):
    '''Draws a pinwheel using rectanglePrint(), rotating and reprinting n times'''
    turnAngle = 360/n;
    for i in range(n):
        rectanglePrint(t,w,h) # HELPER FUNCTION
        t.left(turnAngle)

pinwheel_1(alex,75,150,40)
