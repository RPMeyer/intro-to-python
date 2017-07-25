#*******************************
#ws ch7_3

# randint(n1,n2) from the random module generates
# random ints from n1 to n2 inclusive.
# Write a function a function, ran_walk(t,Dz,n),
# which makes the turtle t move a distance Dz
# in a random direction n times.
# Use helper functions to set up the screen and
# set up the turtle.
#*******************************
import turtle
import random
testTurt = turtle.Turtle()


def turtleInit(bgColor, wnInfo):
    '''initializes turtle'''
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title(wnInfo)

def rand_walk(t,Dz,n):
    '''makes the turtle t move a distance Dz in a random direction n times'''
    # use helper functions to set up the screen and set up the turtle.

    for i in range(n):
        # r = random.randint(0,359)
        t.left(random.randint(0,359))
        t.forward(Dz)
turtleInit('lightgreen', 'random walker')
rand_walk(testTurt, 25, 15)
