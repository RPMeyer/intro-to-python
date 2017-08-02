import turtle
testTurt = turtle.Turtle()
testTurt.speed(1)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("wnInfo")
wn.setworldcoordinates(0, 0, wn.window_width(), wn.window_height())
testTurt.penup()
turtle.tracer(0,0)

def stampShape(color1='blue',color2='red'):
    '''creates shape for stamp, and stamps'''
    createPolys(poly1,poly2,poly3,poly4,color1,color2)
    turn=90
    for i in range(0,4,1):
        testTurt.shape("myshape")
        testTurt.seth(turn)
        testTurt.stamp()
        turn+= 90

def repeatShape(magVal, times, color1, color2):
    '''repeats defined shape with resizing (magVal) value via stamp, (times) times'''
    testTurt.shapesize(magVal)
    i = 0
    trackerY = 61*magVal;
    bounds = wn.screensize()
    stampCount=0
    rowCount=0
    while (True):
        print('i counter is {}'.format(i))

        if (stampCount%4==0):
            colorHold=color1
            color1=color2
            color2=colorHold
            stampShape(color1,color2)
        else:
            stampShape(color1,color2)
        stampCount+=1
        print('bounds are {}'.format(bounds))
        print('stampCount is {}'.format(stampCount))
        if ((testTurt.xcor() >= wn.window_width())):
            testTurt.setpos(0, trackerY)
            stampShape(color1, color2)
            trackerY +=(61*magVal);
            rowCount+=1
            stampCount=0
            stampCount+=1
            if (rowCount%3==0):
                colorHold=color1
                color1=color2
                color2=colorHold
                stampShape(color1,color2)
        testTurt.forward(61*magVal)
        i+=1
        if (testTurt.ycor() >= wn.window_height()) and (testTurt.xcor() >= wn.window_width()):
            stampShape()
            break

def createPolys(poly1,poly2,poly3,poly4,c1,c2):
    '''Creates a new shape that replaces the turtle out of poly1 through poly4. Applies colors c1 and c2 to the specified polys'''
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

#createPolys(poly1,poly2,poly3,poly4,'red','blue')

repeatShape(1, 4, 'blue', 'red')

wn.exitonclick()
