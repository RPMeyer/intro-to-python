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

def draw_rects(t,W1,H1,W2,H2):


#function to run
draw_rects(tess,200,20,25,400)
