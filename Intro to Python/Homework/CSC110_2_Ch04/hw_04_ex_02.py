# Write a program to draw this ( 5 concentric squares of decreasing size) Assume the innermost square is 20 units per side
# each successive square is 20 units bigger (size += to 20), per side, than the one inside it.
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a line of squares")
alex = turtle.Turtle()
alex.speed()

def draw_square(t,sz):
    '''Draws an equilateral polygon of 4 sides (SQUARE) with length sz'''
    for i in range(0,4,1):
        t.forward(sz)
        t.left(360/4)

#USES HELPER FUNCTION draw_square(t,sz)
def draw_concentric_squares(t, sz, n):
    '''Draws concentric polygons of 4 sides (SQUARE) with length sz, n times'''
    for i in range(0,n,1):
        t.penup()
        t.setpos(0.00-.5*sz,0.00-.5*sz)
        t.pendown()
        draw_square(t,sz)
        sz +=20

draw_concentric_squares(alex, 20, 5)
