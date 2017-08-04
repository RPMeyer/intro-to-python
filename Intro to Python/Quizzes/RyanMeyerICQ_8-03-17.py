import turtle,random,time

wn = turtle.Screen()
wn.bgcolor('lightgreen')
wn.title('tess wanders around inside a rectangle')
t = turtle.Turtle()
t.color('blue')
t.pensize(3)
t.speed(5)
#turtle.tracer(0,0)


def isInsideRect(t,W,H):
    '''returns true if turtle t is inside rect of (W)width and (H)height, ceneter at origin'''
    while(True):
        if ((abs(t.ycor()) > .5*H-1) or (abs(t.xcor()) > .5*W-1)):
            return False
        else:
            return True

def rectangle(t,w,h):
    '''Used to draw rectangle of various (w)idth and (h)eight'''
    t.penup()
    t.setpos(-.5*W,-.5*H)
    t.pendown()

    for i in range(0,1+1,1):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def ran_walk_inside_rect(t,W,H,sz):
    '''turtle t executes a random walk, moving distance (sz) in a random direction. Starts at origin (0,0),
    stops first time turtle leaves bounds of rect(W,H)'''
    t.penup()
    t.goto(0,0)
    t.pendown()

    distanceTotal =0
    counter=0
    while(isInsideRect(t,W,H)==True):
        t.left(random.randint(0,359))
        t.forward(sz)
        distanceTotal+=sz
        counter+=1
    print('total distance walked by the turtle is: {} and the total number of steps taken is: {}'.format(distanceTotal, counter))

W,H=600,300

rectangle(t,W,H)
ran_walk_inside_rect(t,W,H,50)

for (x,y) in [(W/4,H/4),(-W/4,-H/4),(W/4,H/2),(W/2,H/4),(W/4,1.2*H/2)]:
    t.setpos(x,y)
    print(x,y,isInsideRect(t,W,H))
    time.sleep(4)
