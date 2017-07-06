# **************************************************
# WS ch4_2
# Write a function, draw_rects(t,W1,H1,W2,H2), which uses Turtle t
# to draw 2 rectangles with the same center. Can you use
# draw_rectangle(t,W,H) as a helper function? Can you write any
# other useful helper functions?

#write func rectangle as helper function. when running draw_rects it rotates.
# use/make dynamic function for turtle position (in this case it will center in rect)
# **************************************************
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex draws a square")
tess = turtle.Turtle()

#HELPER FUNCTION FOR POSITIONING TURTLE DRAW ORIGIN
def turtlePosition(t,penX,penY):
    '''FUNCTION FOR POSITIONING TURTLE DRAW ORIGIN. Moves to penX and penY'''
    t.penup() #don't draw when turtle moves
    t.hideturtle() #make the turtle invisible
    # t.setx(penX) REDUNDENT GIVEN GOTO
    # t.sety(penY) REDUNDENT GIVEN GOTO
    t.goto(penX,penY)
    t.showturtle() #make the turtle visible
    t.pendown() #draw when the turtle moves

#HELPER FUNCTION FOR DRAWING THE RECTANGLES
def draw_square(t,w,h):
    '''Used to draw rectangle of various (w)idth and (h)eight'''
    for i in range(0,1+1,1):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_rects(t,W1,H1,W2,H2):
    '''Draws 2 recangles of (W1)idth, (H1)eight, (W2)idth, (H2)eight using the draw_square() function'''
    draw_square(t,W1,H1)
    turtlePosition(t,(1/2)*W1,-(1/2)*H2) #NEGATIVE H2 SO THAT TURTLE DRAWS THROUGH CENTER OF FIRST RECT (W1)
    draw_square(t,W2,H2)

#function to run
draw_rects(tess,200,20,25,400)
