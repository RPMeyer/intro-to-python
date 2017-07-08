# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# • An equilateral triangle (sides 3)
# • A square (sides 4)
# • A hexagon (six sides)
# • An octagon (eight sides)
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess draws POLYGONS using FOR LOOPS and FUNCTIONS")
testTurt = turtle.Turtle() #CREATES THE TURTLE

def draw_equilatoral(t,n,sz):
    '''draws an equilateral polygon of (n) sides of size (sz) using Turtle (t)'''
    for i in range(0,n,1):
        t.forward(sz)
        t.left(360/n)

# draw_polygon(testTurt,int (input("enter number of sides: ")), 150)
# input("press enter to close: ")
draw_equilatoral(testTurt,3,150)
draw_equilatoral(testTurt,4,150)
draw_equilatoral(testTurt,6,150)
draw_equilatoral(testTurt,8,150)
