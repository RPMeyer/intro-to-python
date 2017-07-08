# A drunk pirate makes a random turn and then takes 100 steps forward,
# makes another random turn, takes another 100 steps, turns another random amount, etc.
# A social science student records the angle of each turn before the next 100 steps are taken.
# Her experimental data is [160, -43, 270, -97, -43, 200, -940, 17, -86].
# (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend.
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess draws Drunk Pirate path")
testTurt = turtle.Turtle() #CREATES THE TURTLE

pirateTurns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

def draw_drunkPirate(t,n,sz):
    '''draws a drunk pirates path with turns (n) and sides of size (sz) using Turtle (t)'''
    for i in n:
        if i >= 0:
            t.left(i)
        else:
            t.right(i)
        t.forward(sz)

draw_drunkPirate(testTurt, pirateTurns, 100)
