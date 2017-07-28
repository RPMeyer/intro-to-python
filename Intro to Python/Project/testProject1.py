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
    '''creates shape from stamp'''
    turn=90
    for i in range(0,4,1):
        testTurt.shape("myshape")
        testTurt.setheading(turn)
        testTurt.stamp()
        turn+= 90

def repeatShape(times):
    '''repeats defined shape (times)times'''
    i = 0
    trackerY = 60;
    bounds = wn.screensize()
    while (i < times):
        createShape()
        print(bounds)
        if (testTurt.xcor() == wn.window_width()):
            testTurt.setpos(0, trackerY)
            createShape()
            trackerY = trackerY +60;
        print(testTurt.pos())
        testTurt.forward(60)
        i+=1

s = turtle.Shape("compound")

#topLeftCorner
poly1 = ((0,0),(20,0),(0,-20))
s.addcomponent(poly1, "red")

poly2 = ((20,0),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(0,-20),(10,-10))
s.addcomponent(poly2, "blue")

poly3 = ((30,-10),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(10,-30))
s.addcomponent(poly3, "red")

poly4 = ((10,-30),(30,-30),(30,-10))
s.addcomponent(poly4, "blue")

wn.register_shape("myshape", s)

repeatShape(13)
wn.exitonclick()
