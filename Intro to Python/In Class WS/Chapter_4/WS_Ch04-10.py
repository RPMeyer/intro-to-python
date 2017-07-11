# **********************************************
# WS ch 4-10
#
# This example is about helper functions, not conditionals.
# **********************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a line of squares")
alex = turtle.Turtle()
alex.speed(100)

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

def repeating_rect_of_line_of_squares(t, sz, n_w, n_h, multiples):
    '''repeats rect_of_line_of_squares() to make squares of squares of squares'''
    for i in range(multiples):
        alex.pendown()
        rect_of_line_of_squares(t, sz, n_w, n_h)
        alex.penup()
        t.forward(2*(sz*n_w))

repeating_rect_of_line_of_squares(alex, 25, 4, 4, 10)
