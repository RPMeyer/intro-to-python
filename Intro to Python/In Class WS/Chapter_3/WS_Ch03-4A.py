# ***************************************
# WS ch3_4A :
# Write a program that uses a for loop to print
# a rectangle using a function, rectangle(t,w,h),
# Using turtle, t, width, w, and height,h.
# ***************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a rectangle using a FUNCTION")
alex = turtle.Turtle() #CREATES THE TURTLE

def rectanglePrint(t,w,h):
    '''Draws a rectangle of width w, height h, using turtle t'''
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

rectanglePrint(alex,150,300)

#input("press ENTER to quit")
