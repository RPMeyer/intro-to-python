# ************************************************
# WS ch4_1
# Write a function, draw_triangle(t,sz), which draws an equilateral
# triangle of size sz using Turtle t.
# *************************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a square")
testTurt = turtle.Turtle()

# def draw_triangle(t,sz):
#     '''draws an equilateral triangle of size sz using Turtle t'''
#     for i in range(0,3,1):
#         t.forward(sz)
#         t.left(360/3)
#
# draw_triangle(testTurt,150)

def draw_polyhedron(t, n, sz):
    '''draws an equilateral polyhedron with n number of sides of size sz using Turtle t'''
    for i in range(0,n,1):
        t.forward(sz)
        t.left(360/n)

draw_polyhedron(testTurt,int (input("enter number of sides: ")), 150)
input("press enter to close: ")
