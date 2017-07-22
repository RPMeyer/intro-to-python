#draw pictures

#YOUTUBE LINK: https://youtu.be/_fFzSBgkYHY

#initial turtle import and initializing starting values for turtle components
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws lots of lines")
alex = turtle.Turtle()
alex.speed(100) #increasing turtle speed to 100


def draw_lines_with_angle(t,sz,n,times):
    '''Draws a line of increasing length that has initial size (sz) with turn angle (n), (times) times'''
    for i in range(0,times+1,1):
        sz += 5
        t.forward(sz)
        t.left(n)

alex.penup()
alex.goto(-250,0) #recenters turtle
alex.pendown()
draw_lines_with_angle(alex, 10, 90, 100) #image one in question 5 - turn anlge of 90 degrees. Line drawn 100 times.

alex.penup()
alex.goto(250,0) #recenters turtle
alex.pendown()
draw_lines_with_angle(alex,10,91,100) #image two in question 5 - with turn angle of 91 degress. Line drawn 100 times
