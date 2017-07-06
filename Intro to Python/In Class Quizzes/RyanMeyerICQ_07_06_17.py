#Ryan Meyer In Class Quiz Thursday, July 06th

#Write a function, line_of_squares(t,sz,n), which draws a LINE of n SQUARES, each of SIZE sz, connected together.
#For full credit, use draw_square(t,sz) as a helper function in the deifnition of line_of_squares(t,sz,n).

# Sample Run: line_of_squares(alex, 75, 5)

#importing TURTLE library and creating new turtle for manipulation
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a line of squares")
alex = turtle.Turtle()

#***********not entirely needed, but output looks better
alex.penup()
alex.goto(-200,0)
alex.pendown()
#*****************


#HELPER FUNCTION draw_square(t,sz)
def draw_square(t,sz):
    '''Draws an equilateral polygon of 4 sides (SQUARE) with length x'''
    for i in range(0,4,1):
        t.forward(sz)
        t.left(360/4)

#draw_square(alex,50) #testing turtle drawing of square function

def line_of_squares(t, sz, n):
    '''Draws a line of n SQUARES, each of size sz. Uses draw_square() as a helper'''
    for i in range(0, n, 1):
        draw_square(t,sz)
        t.forward(sz)

line_of_squares(alex, 75, 5)
