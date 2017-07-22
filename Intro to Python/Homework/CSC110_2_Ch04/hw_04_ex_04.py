#Draw pattern
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
def draw_square_repeating_with_turn(t,sz,n):
    '''Draws a square repeatedlky turning n degrees'''
    for i in range(0,int(360/n),1):
        draw_square(t,sz)
        t.left(n)
draw_square_repeating_with_turn(alex, 100, 18)
