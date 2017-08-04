import turtle
testTurt = turtle.Turtle()
testTurt.speed(1)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("wnInfo")
testTurt.penup()
turtle.tracer(0,0)

def createPolys(poly1,poly2,poly3,poly4,color1,color2):
    '''Creates a new shape that replaces the turtle out of poly1 through poly4. Applies colors c1 and c2 to the specified polys'''
    s = turtle.Shape("compound")

    s.addcomponent(poly1, color1)
    s.addcomponent(poly2, color2)
    s.addcomponent(poly3, color1)
    s.addcomponent(poly4, color2)

    wn.register_shape("myshape", s)

def swapColors(color1,color2,colorHold=''):
    '''uses colorHolder variable to effectively swap color1 and color2, then returns color1 and color2'''
    colorHold=color1
    color1=color2
    color2=colorHold
    return color1,color2

def stampShape(color1='blue',color2='red'):
    '''creates shape for stamp, and stamps'''
    createPolys(poly1,poly2,poly3,poly4,color1,color2)
    turn=90
    for i in range(0,4,1):
        testTurt.shape("myshape")
        testTurt.seth(turn)
        testTurt.stamp()
        turn+= 90

def createSquare(magVal, color1='blue', color2='red'):
    shapeSize=61*magVal

    for n in range(0,4,1):
        for i in range(0,4,1):
            stampShape(color1,color2)
            testTurt.forward(shapeSize)
        testTurt.forward(-4*shapeSize)
        testTurt.left(90)
        testTurt.forward(shapeSize)
        testTurt.right(90)
    return testTurt.pos()

def createPattern(magVal,color1,color2, times):
    '''creates a pattern of createSquare() as a (times)x(times) squares with alternating colors'''
    shapeSize=61*magVal
    bounds=shapeSize*times*times

    wn.setup(width=bounds-shapeSize, height=bounds-shapeSize, startx=None, starty=None)
    wn.setworldcoordinates(0, 0, wn.window_width(), wn.window_height())
    testTurt.penup()

    n=0
    testTurt.shapesize(magVal)
    while(True):
        testTurt.goto(shapeSize*n,0)
        for i in range(0,times,1):
            if not i%2==0:
                createSquare(magVal,color1,color2)
                n+=1
            if i%2==0:
                createSquare(magVal,color2,color1)
                n+=1
        color1,color2=swapColors(color1,color2)
        if n==16:
            break

poly1 = ((0,0),(20,0),(0,-20))
poly2 = ((20,0),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(0,-20),(10,-10))
poly3 = ((30,-10),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(10,-30))
poly4 = ((10,-30),(30,-30),(30,-10))

#createPolys(poly1,poly2,poly3,poly4,'red','blue')

createPattern(.75,'blue', 'red',4)

wn.exitonclick()
