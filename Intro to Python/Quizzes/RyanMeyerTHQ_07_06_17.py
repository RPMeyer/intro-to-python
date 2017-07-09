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

def line_of_squares(t, sz, n):
    '''Draws a line of n SQUARES, each of size sz. Uses draw_square() as a helper'''
    for i in range(0, n, 1):
        draw_square(t,sz)
        t.forward(sz)

def rect_of_line_of_squares(t, sz, n_w, n_h):
    '''Makes a rectangle of squares of WIDTH (sz *n_w) and HEIGHT (sz * n_h) ... etc ...'''
    if n_w and n_h >= 1:
        for i in range(0,1+1,1):
            line_of_squares(t,sz,n_w) #line of squares using n_w
            t.left(90)
            line_of_squares(t,sz,n_h) #line of squares using n_h
            t.left(90)
    else:
        print("Use intergers larger than or equal to 1")

rect_of_line_of_squares(alex, 25, 8,4)
