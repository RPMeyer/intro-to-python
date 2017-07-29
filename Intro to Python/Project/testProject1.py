import turtle
testTurt = turtle.Turtle()
#testTurt.speed(1)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("wnInfo")
wn.setworldcoordinates(0, 0, wn.window_width(), wn.window_height())
testTurt.penup()
turtle.tracer(0,0)

def createShape():
    '''creates shape for stamp, and stamps'''
    turn=90
    for i in range(0,4,1):
        testTurt.shape("myshape")
        testTurt.seth(turn)
        testTurt.stamp()
        turn+= 90

def repeatShape(magVal):
    '''repeats defined shape with resizing (magVal) value via stamp'''
    testTurt.shapesize(magVal)
    i = 0
    trackerY = 61*magVal;
    bounds = wn.screensize()
    while (True):
        print(i)
        createShape()
        print(bounds)
        if  (testTurt.xcor() >= wn.window_width()):
            testTurt.setpos(0, trackerY)
            createShape()
            trackerY +=(61*magVal);
        print(testTurt.pos())
        testTurt.forward(61*magVal)
        i+=1
        if (testTurt.ycor() >= wn.window_height()) and (testTurt.xcor() >= wn.window_width()):
            createShape()
            break

def createPolys(poly1,poly2,poly3,poly4,c1,c2):
    '''Creates a new shape that replaces the turtle ouot of poly1 through poly4. Applies colors c1 and c2 to the specified polys'''
    s = turtle.Shape("compound")

    s.addcomponent(poly1, c1)
    s.addcomponent(poly2, c2)
    s.addcomponent(poly3, c1)
    s.addcomponent(poly4, c2)

    wn.register_shape("myshape", s)

poly1 = ((0,0),(20,0),(0,-20))
poly2 = ((20,0),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(0,-20),(10,-10))
poly3 = ((30,-10),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(10,-30))
poly4 = ((10,-30),(30,-30),(30,-10))

createPolys(poly1,poly2,poly3,poly4,'red','blue')

repeatShape(1)

wn.exitonclick()
