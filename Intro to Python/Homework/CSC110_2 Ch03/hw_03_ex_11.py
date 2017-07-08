# Write a program to draw a shape like this:
# Hints:
# • Try this on a piece of paper, moving and turning your cellphone as if it was a turtle.
#     Watch how many complete rotations your cellphone makes before you complete the star.
#     Since each full rotation is 360 degrees, you can figure out the total number of degrees
#     that your phone was rotated through. If you divide that by 5, because there are five points
#     to the star, you’ll know how many degrees to turn the turtle at each point.
# • You can hide a turtle behind its invisibility cloak if you don’t want it shown. It will
#     still draw its lines if its pen is down. T he method is invoked as tess.hideturtle().
#     To make the turtle visible again, use tess.showturtle()
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess draws POLYGONS using FOR LOOPS and FUNCTIONS")
testTurt = turtle.Turtle() #CREATES THE TURTLE

#NOT PERFECT. THERE ARE MULTIPLE EQUATIONS FOR DIFFERENT 'STARS'
def draw_nonConvex(t,n,sz):
    '''draws a NONCONVEX equilateral polygon with number of sides (n) of size (sz) using Turtle (t)'''
    for i in range(0,n,1):
        t.forward(sz)
        t.left(180-(1-(6/n))*180)

draw_nonConvex(testTurt, 5, 150)
