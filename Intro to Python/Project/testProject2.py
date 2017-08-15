#YOUTUBE VIDEO of powerpoint: https://youtu.be/DhLMyyw6-X8
import turtle
testTurt = turtle.Turtle()
testTurt.speed(1)
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("wnInfo")
testTurt.penup()
turtle.tracer(0,0)

def createPolys(poly1,poly2,poly3,poly4,color1,color2):
    '''Registers a new shape that replaces the turtle out of poly1 through poly4. Applies colors c1 and c2 to the specified polys'''
    s = turtle.Shape("compound")

    s.addcomponent(poly1, color1)
    s.addcomponent(poly2, color2)
    s.addcomponent(poly3, color1)
    s.addcomponent(poly4, color2)

    wn.register_shape("myshape", s)
    #registers the user created shape to later be used as the turtle
    #thus allowing the stamp methods to create the pattern

def stampShape(color1='blue',color2='red'):
    '''creates shape for stamp, and stamps'''
    createPolys(poly1,poly2,poly3,poly4,color1,color2)
    turn=90
    #rotates the turtle 4 times in a circle to create the simple shape of the pattern - specified via createPolys
    for i in range(0,4,1):
        testTurt.shape("myshape")
        testTurt.seth(turn)
        testTurt.stamp()
        turn+= 90

def createSquare(magVal, color1='blue', color2='red'):
    '''creates the square that composes the desired pattern. The pattern is the turtle shape repeated 4 times, then repeating that 4 more times'''
    shapeSize=61*magVal

    for n in range(0,4,1):
        for i in range(0,4,1):
            stampShape(color1,color2)
            testTurt.forward(shapeSize)
        testTurt.forward(-4*shapeSize)
        testTurt.left(90)
        testTurt.forward(shapeSize)
        testTurt.right(90)
    return testTurt.pos() #used for debugging - not entirely necessary in current code factor

def swapColors(color1,color2,colorHolder=''):
    '''uses colorHolder variable to effectively swap color1 and color2, then returns color1 and color2'''
    colorHolder=color1
    color1=color2
    color2=colorHolder
    return color1,color2

def createPattern(magVal,color1,color2, times):
    '''creates a pattern of createSquare() as a (times)x(times) square with alternating colors.
    Squares changed in size via magVal'''
    shapeSize=61*magVal
    bounds=shapeSize*times*4 #useful in determining if turtle is out of bounds, but primarily used to get screensize, 4 because squares are 4x4 individually

    wn.setup(width=bounds-shapeSize, height=bounds-shapeSize, startx=None, starty=None) #sets up the windows dimensions for ease of viewing
    wn.setworldcoordinates(0, 0, wn.window_width(), wn.window_height()) #starts turtle creating pattern in bottom left corner
    testTurt.penup()

    squareCount=0
    x=0
    testTurt.shapesize(magVal) #resizes the pattern with a multiplier of magVal
    while(True):
        testTurt.goto(shapeSize*x*4,0) #prevents turtle from creating squares on top of squares on top of squares, and moves appropriate x-distance
        x+=1
        for i in range(0,times,1): #used to facilitate the swapping of colors and create the appropriate number of squares
            if not i%2==0:
                createSquare(magVal,color1,color2)
                squareCount+=1
            elif i%2==0:
                createSquare(magVal,color2,color1)
                squareCount+=1
        color1,color2=swapColors(color1,color2) #assigns the new color values after being swapped after the if statement is executed
        if squareCount==(times*times): #16 due to being 4 x 4 square
            break

#------------------------------------
# IMPORTANT - backbone of the pattern
#
# values assigned to create individual polygons that compose the appropriate shape/pattern to be replicated.
# each poly is a tupel composed of the points in a (x,y) plane that create said polygon.
#------------------------------------
poly1 = ((0,0),(20,0),(0,-20))
poly2 = ((20,0),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(0,-20),(10,-10))
poly3 = ((30,-10),(30,0),(20,-10),(10,-10),(10,-20),(0,-30),(10,-30))
poly4 = ((10,-30),(30,-30),(30,-10))

createPattern(1,'black', 'blue',4)

wn.exitonclick()
