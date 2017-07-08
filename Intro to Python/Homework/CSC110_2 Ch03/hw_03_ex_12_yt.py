#Write a program to draw a face of a clock:
#Include tick marks for the hour and have a 'turtle' denote each hour (12)

#Youtube link: https://youtu.be/k7ZDLqHShgI

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("testTurt draws clock from book")
testTurt = turtle.Turtle() #CREATES THE TURTLE
testTurt.color("blue")
testTurt.shape("turtle")

#'simple' solution to create the clock as per the supplied image
for i in range(0,12,1):
    testTurt.goto(0,0) #resets the turtles position at the beginning of the loop. Avoids starting from the last position drawn.
    testTurt.penup() #prevents turtle from drawing the entire time it is moving
    testTurt.forward(250) #movement
    testTurt.pendown() #allows drawing
    testTurt.forward(20) #draws hour tick mark
    testTurt.penup() #stops drawing to enable movement further for the turtle to be stamped
    testTurt.forward(10) #movement without drawing
    testTurt.stamp() #stamps turtle 10 ahead of the hour tick mark
    testTurt.left(30) #turns turt 30 degrees to prep for new hour tick
