# Write a void (non-fruitful) function to draw a square. Use it in a program to draw the
# image shown below. Assume each side is 20 units. (Hint: notice that the turtle has
# already moved away from the ending point of the last square when the program ends.)
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
        t.penup()
        t.forward(2*sz)
        t.pendown()

line_of_squares(alex, 20, 5)
